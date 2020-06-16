import pdb_extr 
import os
import gzip
import re
import csv
import copy

outputfile = 'metadata_tabs_nodubl.csv'

pdb_folders_location = '/home/axel/Documents/DataScience/projects/pdb/pdb'
pdb_folders = os.listdir(pdb_folders_location)

empty_dict = {'DATE': '01/01/1900',
              'pdb_entry': 'NA',
              'SOURCE_EXPRESSION_SYSTEM_TAXID': [], 
              'SOURCE_ORGANISM_TAXID': [],
              'KEYWDS': [],
              'EXPDTA': 'NA', 
              #'JRNL_REF': 'NA',
              #'JRNL_PMID': 'NA',
              'JRNL_DOI': [],
              'RESOLUTION': -1,
              'REFINEMENT_PROGRAM': 'NA',
              #'PROTEIN_ATOMS': -1,
              #'HETEROGEN_ATOMS': -1,
              #'SOLVENT_ATOMS': -1,
              #'MEAN_B_VALUE': -1,
              #'EXPERIMENT_TYPE': 'NA',
              #'DATE_DATA_COLLECTION': '01/01/1900',
              'TEMPERATURE_K': -1,
              'pH': -1,
              'SYNCHROTRON': 'NA',
              'RADIATION_SOURCE': 'NA',
              'BEAMLINE': 'NA',
              #'X_RAY_GENERATOR_MODEL': 'NA',
              #'WAVELENGTH_RANGE': -1,
              #'DETECTOR_TYPE': 'NA',
              #'DETECTOR_MANUFACTURER': 'NA',
              'INTENSITY_INTEGRATION_SOFTWARE': 'NA',
              'DATA_SCALING_SOFTWARE': 'NA',
              #'NO_UNIQUE_REFLECTIONS': -1,
              #'RESOLUTION_RANGE_HIGH': -1,
              #'RESOLUTION_RANGE_LOW': -1,
              #'REJECTION_CRITERIA': 'NA',
              #'DATA_REDUNDANCY': -1,
              #'DIFFRACTION_PROTOCOL': 'NA', 
              'METHOD_TO_DETERMINE_STRUCTURE': 'NA',
              'SOFTWARE_TO_DETERMINE_STRUCTURE': 'NA', 
              'STARTING_MODEL': 'NA',
              'SOLVENT_CONTENT': -1,
              'MATTHEWS_COEFFICIENT': -1,
              'HETNAM': [],
              'CRYST': 'NA'
             }

keys_4_headers = list(empty_dict.keys())
headers_out = '\t'.join(keys_4_headers)

with open(outputfile, 'w') as o:
    o.write(headers_out.strip() + '\n')

# compiled regexes
expr_sys = re.compile('EXPRESSION_SYSTEM_TAXID')
organism_id = re.compile('ORGANISM_TAXID')
jrnl_doi = re.compile('^JRNL\s+DOI')
resolution = re.compile('^REMARK\s+2\s+RESOLUTION')
refinement_software = re.compile('^REMARK\s+3\s+PROGRAM')
temperature = re.compile('^REMARK\s+200\s+TEMPERATURE.+KELVIN')
pH = re.compile('^REMARK\s+200\s+PH')
synchrotron = re.compile('^REMARK\s+200\s+SYNCHROTRON')
radiation_source = re.compile('^REMARK\s+200\s+RADIATION SOURCE')
beamline = re.compile('^REMARK\s+200\s+BEAMLINE\s*:')
#beamline = re.compile('^REMARK\s+200\s+BEAMLINE') This picks up random mentions of beamline
intensity_integration = re.compile('^REMARK\s+200\s+INTENSITY-INTEGRATION SOFTWARE')
scaling_software = re.compile('^REMARK\s+200\s+DATA SCALING SOFTWARE')
structure_method = re.compile('^REMARK\s+200\s+METHOD USED TO DETERMINE THE STRUCTURE')
mr_software = re.compile('^REMARK 200 SOFTWARE USED')
starting_model = re.compile('^REMARK\s+200\s+STARTING MODEL')
solvent_content = re.compile('^REMARK 280 SOLVENT CONTENT')
matthews = re.compile('^REMARK 280 MATTHEWS COEFFICIENT')
#


# pdb_location =  pdb_folders_location + '/' + pdb_folders[0]
pdb_location = ['/'.join([pdb_folders_location,item]) for item in pdb_folders]


temp_dict = copy.deepcopy(empty_dict)

pdbs = []

for pdb_location_item in pdb_location:
    for pdb in os.listdir(pdb_location_item):
        pdb_path = pdb_location_item + '/' + pdb
        if pdb_path.endswith(".gz"):
            pdbs.append(pdb_path)

for pdb in pdbs:
    temp_dict = copy.deepcopy(empty_dict)
    with gzip.open(pdb, 'rt') as f:
        with open(outputfile, 'a') as o:
            for line in f:
                if  re.match('^HEADER', line):
                    out_dict = pdb_extr.header_extract(line)
                    temp_dict.update(out_dict)
                elif expr_sys.search(line):
                    temp_dict['SOURCE_EXPRESSION_SYSTEM_TAXID'].append(pdb_extr.expression_taxid_extract(line))
                elif organism_id.search(line):
                    temp_dict['SOURCE_ORGANISM_TAXID'] = pdb_extr.source_organsim_taxid_extract(line)
                elif re.match('^KEYWDS', line):
                    temp_dict['KEYWDS'] = pdb_extr.keywords_extract(line)
                elif re.match('^EXPDTA', line):
                    temp_dict.update(pdb_extr.experimental_method_extract(line))
                elif jrnl_doi.search(line):
                    temp_dict['JRNL_DOI'].append(pdb_extr.journal_doi_extract(line))
                elif resolution.search(line):
                    temp_dict.update(pdb_extr.resolution_extract(line))
                elif refinement_software.search(line):
                    temp_dict.update(pdb_extr.refinement_program_extract(line))
                elif temperature.search(line):
                    temp_dict.update(pdb_extr.temperature_extract(line))
                elif  pH.search(line):
                    temp_dict.update(pdb_extr.pH_extract(line))
                elif  synchrotron.search(line):
                    temp_dict.update(pdb_extr.is_synchrotron(line))
                elif radiation_source.search(line):
                    temp_dict.update(pdb_extr.radiation_source_extract(line))
                elif beamline.search(line):
                    temp_dict.update(pdb_extr.which_beamline(line))
                elif intensity_integration.search(line):
                    temp_dict.update(pdb_extr.which_intensity_integration_software(line))
                elif scaling_software.search(line):
                    temp_dict.update(pdb_extr.which_scaling_software(line))
                elif structure_method.search(line):
                    temp_dict.update(pdb_extr.which_method_of_structure_determination(line))
                elif mr_software.search(line):
                    temp_dict.update(pdb_extr.which_software_struture_determination(line))
                elif starting_model.search(line):
                    temp_dict.update(pdb_extr.which_model(line))
                elif solvent_content.search(line):
                    temp_dict.update(pdb_extr.solvent_content_extract(line))
                elif matthews.search(line):
                    temp_dict.update(pdb_extr.matthews_extract(line))
                elif re.match('^HETNAM', line):
                    temp_dict['HETNAM'].append(pdb_extr.hetnam_extract(line))
                elif re.match('^CRYST', line):
                    temp_dict.update(pdb_extr.unit_cell_extract(line))
                    dict_values = list(temp_dict.values())
                    out_string = '\t'.join([str(elem) for elem in dict_values])
                    o.write(out_string + '\n')



