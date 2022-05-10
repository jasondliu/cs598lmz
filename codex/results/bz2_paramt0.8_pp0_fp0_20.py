from bz2 import BZ2Decompressor
BZ2Decompressor

print('boto: ' + boto.__version__)
print('botocore: ' + botocore.__version__)
print(glue.__version__)
print(psycopg2.__version__)
print(pandas.__version__)

# s3 path
s3_bucket = 'dpa-metro-dados'
s3_prefix = 'dados-abertos/rdados'
s3_temp_path = 'temp'
s3_input_path = 'entrada'
s3_output_path = 'saida'
s3_name = 'rdados'
s3_suffix = '.csv.bz2'
s3_paths = {
    'input': f's3://{s3_bucket}/{s3_prefix}/{s3_input_path}/',
    'output': f's3://{s3_bucket}/{s3_prefix}/{s3_output_path}/',
    'temp': f's3://{s3_buck
