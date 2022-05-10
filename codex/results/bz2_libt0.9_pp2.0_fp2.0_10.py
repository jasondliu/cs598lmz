import bz2
bz2.BZ2File

def load_file(filename, output_file):
    with bz2.BZ2File(filename, mode='r') as f:
        conteudo = f.readlines()

        with open(output_file, mode='w') as f2:
            for line in conteudo:
                f2.write(line.decode('utf-8'))

input_file_name = '../testes/features_Input.csv.bz2'
output_file_name = '../testes/features_Output.csv'

load_file(input_file_name, output_file_name)
