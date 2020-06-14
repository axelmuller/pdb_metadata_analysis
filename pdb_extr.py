import pandas as pd
import numpy as np
import re
import  string

def error():
    """returns an error message"""
    return('ERROR CHECK ENTRY')

def header_extract(header):
    """Extracts date of submission and pdb Id into a dictionary"""
    split = header.split()
    try:
        out_dict = {'DATE': split[-2], 
                    'pdb_entry': split[-1]}
    except:
        out_dict = {}
    return(out_dict)


def expression_taxid_extract(expression_system_taxid_entry):
    """Exctracts the TAXID of the expression system"""
    # this might run into problems if multiple expression systems are used
    try:
        split = expression_system_taxid_entry.split(':')[1].strip()
    except:
        split = 'ERROR'
    return(split)
    

def source_organsim_taxid_extract(source_taxid):
    """Extracts the TAXID of the source organism"""
    try:
        taxid = source_taxid.split(':')[1].strip()
        # strip punctuation
        taxid = taxid.translate(str.maketrans('', '', string.punctuation))
    except:
        taxid = 'ERROR'
    return(taxid)

def keywords_extract(keywds_info):
    """Extracts Keywords associated with PDB entry"""
    # Potential problem: KEYWDS might cover multiple lines
    try:
        keywords = keywds_info.split()[1:]
    except:
        keywords = ['ERROR']
    return(keywords)

def experimental_method_extract(expdta):
    """Extracts the experimental method applied"""
    try:
        method = expdta.split(' ', 1)[1].strip()
        out_dict = {'EXPDTA': method}
    except:
        out_dict = {'EXPDTA': 'ERROR'}
    return(out_dict)

def journal_doi_extract(journal_doi):
    """Extracts the doi for the publication """
    doi = journal_doi.split()[-1]
    return(doi)

def resolution_extract(resolution):
    """Extracts the resolution"""
    resolution_A = resolution.split()[-2]
    out_dict = {'RESOLUTION': resolution_A}
    return(out_dict)

def refinement_program_extract(refinement_program):
    """Extracts the refinement program used"""
    software = refinement_program.split(':')[-1].strip()
    out_dict = {'REFINEMENT_PROGRAM': software}
    return(out_dict)

def number_of_protein_atoms(protein_atoms):
    """Extracts the number of protein atoms in the structure"""
    # leave for later
    pass

def temperature_extract(kelvin):
    """Extracts the temperature in K for the experiment"""
    temperature = kelvin.split()[-1]
    out_dict = {'TEMPERATURE_K': temperature}
    return(out_dict)

def pH_extract(pH_info):
    """Extracts the pH for the experiment"""
    pH = pH_info.split()[-1]
    out_dict = {'pH': pH}
    return(out_dict)

def is_synchrotron(synchrotron_question):
    """Was the data collected at a synchrotron?"""
    syncrotron_answer = synchrotron_question.split()[-1]
    out_dict = {"SYNCHROTRON": syncrotron_answer}
    return(out_dict)

def radiation_source_extract(radiation_source_info):
    """Extracts the radiation source"""
    radiation_source = radiation_source_info.split(':')[-1].strip()
    out_dict = {"RADIATION_SOURCE": radiation_source}
    return(out_dict)

def which_beamline(beamline_info):
    """Extracts beamline information"""
    beamline = beamline_info.split(':')[-1].strip()
    out_dict = {'BEAMLINE': beamline}
    return(out_dict)

def which_intensity_integration_software(software_info):
    """Extracts the integration software used"""
    try:
        intensity_software = software_info.split(':')[1].strip()
        out_dict = {'INTENSITY_INTEGRATION_SOFTWARE': intensity_software}
    except:
        out_dict = {'INTENSITY_INTEGRATION_SOFTWARE': 'ERROR'}
    return(out_dict)

def which_scaling_software(scaling_info):
    """Extracts the scaling software used"""
    try:
        scaling_software = scaling_info.split(':')[1].strip()
        out_dict = {'DATA_SCALING_SOFTWARE': scaling_software}
    except:
        out_dict = {'DATA_SCALING_SOFTWARE': 'ERROR'}
    return(out_dict)

def which_method_of_structure_determination(structure_method_info):
    """Extracts information on how the structure was determined"""
    try:
        structure_method = structure_method_info.split(':')[1].strip()
        out_dict = {'METHOD_TO_DETERMINE_STRUCTURE': structure_method}
    except:
        out_dict = {'METHOD_TO_DETERMINE_STRUCTURE': 'ERROR'}
    return(out_dict)

def which_software_struture_determination(structure_software):
    """Extracts software used for structure determination"""
    try:
        software = structure_software.split(':')[1].strip()
        out_dict = {'SOFTWARE_TO_DETERMINE_STRUCTURE': software}
    except:
        out_dict = {'SOFTWARE_TO_DETERMINE_STRUCTURE': 'ERROR'}
    return(out_dict)

def which_model(model_info):
    """Extracts pdb entry used for structure determination"""
    try:
        model = model_info.split(':')[1].strip()
        out_dict = {'STARTING_MODEL': model}
    except:
        out_dict = {'STARTING_MODEL': 'ERROR'} 
    return(out_dict)

def solvent_content_extract(solvent_content_info):
    """Extract solvent content"""
    try:
        solvent_content = solvent_content_info.split(':')[1].strip()
        out_dict = {'SOLVENT_CONTENT': solvent_content}
    except:
        out_dict = {'SOLVENT_CONTENT': 'ERROR'}
    return(out_dict)

def matthews_extract(matthews_info):
    """Extract Matthew's coefficient """
    try:
        matthews = matthews_info.split(':')[1].strip()
        out_dict = {'MATTHEWS_COEFFICIENT': matthews}
    except:
        out_dict = {'MATTHEWS_COEFFICIENT': 'ERROR'}
    return(out_dict)

def hetnam_extract(hetnam_info):
    """Extracts names of hetero molecules in structure"""
    # this is likely to occur several times, make sure all values are maintained
    # hetnam = hetnam_info.split(' ',2)[1].strip()
    try:
        hetnam = ' '.join(hetnam_info.split()[2:])
    except:
        hetnam = 'ERROR'
    return(hetnam)

def unit_cell_extract(cryst_info):
    """Extracts unit cell parameters"""
    try:
        cryst = cryst_info.split(' ', 1)[1].strip()
        out_dict = {'CRYST': cryst}
    except:
        out_dict = {'CRYST': 'ERROR'}
    return(out_dict)

def update_dict_list(reference_dictionary, key2update, new_list):
    """Appends to a list value of the reference dictionary"""
    return(reference_dictionary[key2update].append(new_list))

def update_dict_value(reference_dictionary, key2update, new_value):
    reference_dictionary[key2update] = new_value
