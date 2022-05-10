import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# This file should be copied to the src/main/resources directory in the project
# It will be used by the JUnit tests to check that the transforms are working
#
# The tests will fail unless the file is in the correct place
#

#
# These are the test files that will be used to check the transforms
#

# The test file should be a valid mzML file
mzml_file = "../../resources/mzML_example_files/QC_Shew_Intact_26Sep14_Bane_C2Column3.mzML"

# The test file should be a valid mzML file
traML_file = "../../resources/traML_example_files/QC_Shew_Intact_26Sep14_Bane_C2Column3.traML"

# This is an example of the output from the PeptideProphet algorithm
peptideprophet_file = "../../resources/peptideprophet_example_files/pep.xml"

# This is an
