import ctypes
ctypes.windll.engine.set_dpi_awareness()

# nltk.download('wordnet') # uncomment this line the first time you use the code

parser = argparse.ArgumentParser(description='Input file name')
parser.add_argument('-i', metavar='input', type=str, nargs='+',
                    help='a file to run the code on.')

args = parser.parse_args()

input_file_name = args.i[0]

# input_file_name = 'Programming_Preliminaries_and_Pattern_Matching.txt'
# input_file_name = 'Evaluating_and_Matching_Patterns.txt'
# input_file_name = 'Modular_and_Systematic_Programming.txt'
# input_file_name = 'Procedures_and_the_Processes_They_Generate.txt'
# input_file_name = 'Recursion.txt'
# input_file_name = 'Compound_Data.txt'
# input_file_name = 'Adapt
