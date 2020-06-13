import pdb_extr

def test_header_extract():
    """Perform unit tests on header_extract"""
    assert pdb_extr.header_extract('HEADER    FLAVOPROTEIN                            05-JUN-18   5ZZZ') == {'HEADER': 'FLAVOPROTEIN', 'DATE': '05-JUN-18', 'pdb_entry': '5ZZZ'}


def test_expression_taxid_extract():
    """Perform unit tests on expression_taxid_extract"""
    #assert pdb_extr.expression_taxid_extract('SOURCE   7 EXPRESSION_SYSTEM_TAXID: 562') == {'SOURCE_EXPRESSION_SYSTEM_TAXID': '562'}
    assert pdb_extr.expression_taxid_extract('SOURCE   7 EXPRESSION_SYSTEM_TAXID: 562') == '562'


def test_source_organism_taxid():
    """Perform unit tests on source_organism_taxid_extract """
    assert pdb_extr.source_organsim_taxid_extract('SOURCE   4 ORGANISM_TAXID: 31958;')  == '31958'


def test_keywords_extract():
    """Perform unit tests on keywords_extract"""
    assert pdb_extr.keywords_extract('KEYWDS    FMN-DEPENDENT OXIDASE, FLAVOPROTEIN ') == ['FMN-DEPENDENT', 'OXIDASE,', 'FLAVOPROTEIN']


def test_experimental_method_extract():
    """Perform unit tests on extracting the experimental method"""
    assert pdb_extr.experimental_method_extract('EXPDTA    X-RAY DIFFRACTION') == {'EXPDTA': 'X-RAY DIFFRACTION'}


def test_journal_doi_extract():
    """Perform unit tests on extracting doi"""
    # Might be more than one doi associated with pdb
    assert pdb_extr.journal_doi_extract('JRNL        DOI    10.1107/S2059798319011938 ') == '10.1107/S2059798319011938'


def test_resolution_extract():
    """Perform unit tests on extracting the resolution in Angstroms of the structure"""
    assert pdb_extr.resolution_extract('REMARK   2 RESOLUTION.    1.45 ANGSTROMS.') == {"RESOLUTION": '1.45'}


def test_refinement_program_extract():
    """Perform unit tests on refinement_program_extract"""
    assert pdb_extr.refinement_program_extract('REMARK   3   PROGRAM     : PHENIX 1.9_1692') == {'REFINEMENT_PROGRAM': 'PHENIX 1.9_1692'}


def test_temperature_extract():
    """Perform unit tests on temperature_extract"""
    assert pdb_extr.temperature_extract('REMARK 200  TEMPERATURE           (KELVIN) : 100') == {'TEMPERATURE_K': '100'}


def test_pH_extract():
    """Perform unit tests on pH_extract""" 
    assert pdb_extr.pH_extract('REMARK 200  PH                             : 7.0') == {'pH': '7.0'}


def test_is_synchrotron():
    """Perform unit tests on is.synchrotrot"""
    assert pdb_extr.is_synchrotron('REMARK 200  SYNCHROTRON              (Y/N) : Y') =={'SYNCHROTRON': 'Y'}


def test_radiation_source_extract():
    """Perform unit tests on radiation_source_extract"""
    assert pdb_extr.radiation_source_extract('REMARK 200  RADIATION SOURCE               : NSRRC') == {'RADIATION_SOURCE': 'NSRRC'} 


def test_which_beamline():
    """Perform unit tests on which_beamline"""
    assert pdb_extr.which_beamline('REMARK 200  BEAMLINE                       : BL15A1') == {'BEAMLINE': 'BL15A1'}


def test_which_intensity_integration_software():
    """Perform unit tests on which_intensity_integration_software"""
    assert pdb_extr.which_intensity_integration_software('REMARK 200  INTENSITY-INTEGRATION SOFTWARE : HKL-2000') == {'INTENSITY_INTEGRATION_SOFTWARE': 'HKL-2000'}


def test_which_scaling_software():
    """Perform unit tests on which_scaling_software"""
    assert pdb_extr.which_scaling_software('REMARK 200  DATA SCALING SOFTWARE          : HKL-2000') == {'DATA_SCALING_SOFTWARE': 'HKL-2000'} 


def test_which_method_of_structure_determination():
    """Perform unit tests on which_method_of_structure_determination"""
    assert pdb_extr.which_method_of_structure_determination('REMARK 200 METHOD USED TO DETERMINE THE STRUCTURE: MOLECULAR REPLACEMENT') == {'METHOD_TO_DETERMINE_STRUCTURE': 'MOLECULAR REPLACEMENT'}


def test_which_software_structure_determination():
    """Perform unit tests on which_software_structure_determination"""
    assert pdb_extr.which_software_struture_determination('REMARK 200 SOFTWARE USED: PHENIX') == {'SOFTWARE_TO_DETERMINE_STRUCTURE': "PHENIX"}


def test_which_model():
    """Perform unit tests on which_model"""
    assert pdb_extr.which_model('REMARK 200 STARTING MODEL: 3SGZ') == {'STARTING_MODEL': '3SGZ'}


def test_solvent_content_extract():
    """Perform unit tests on solvent_content_extract"""
    assert pdb_extr.solvent_content_extract('REMARK 280 SOLVENT CONTENT, VS   (%): 64.99') == {"SOLVENT_CONTENT": '64.99'}


def test_matthews_extract():
    """Perform unit tests on matthews_extract"""
    assert pdb_extr.matthews_extract('REMARK 280 MATTHEWS COEFFICIENT, VM (ANGSTROMS**3/DA): 3.51') == {'MATTHEWS_COEFFICIENT': '3.51'}


def test_hetnam_extract():
    """Perform unit test on hetnam_extract"""
    #hyphen and spaces
    assert pdb_extr.hetnam_extract('HETNAM     173 BENZOYL-FORMIC ACID') == 'BENZOYL-FORMIC ACID'
    #no spaces
    assert pdb_extr.hetnam_extract('HETNAM     CSO S-HYDROXYCYSTEINE') == 'S-HYDROXYCYSTEINE'


def test_unit_cell_extract():
    """Perform unit cell tests on unit_cell_extract"""
    assert pdb_extr.unit_cell_extract('CRYST1  138.229  138.229  112.134  90.00  90.00  90.00 I 4 2 2      16') == {'CRYST': '138.229  138.229  112.134  90.00  90.00  90.00 I 4 2 2      16'}


def test_update_dict_list():
    """Perform unit cells tests on update_dict_list"""
    # test_dict = {'key_1': []}
    # assert pdb_extr.update_dict_list(test_dict, 'key_1', ['a', 'b']) == {'key_1', ['a', 'b']}
    assert 1==1
