from bz2 import BZ2Decompressor
BZ2Decompressor()

# Identify current working directory
# When the notebook starts all environment variables are set to their default values defined in the .env file

cwd = os.getcwd()
print(cwd)
 
# Read and store environment variables from .env file

if (platform.system() == 'Linux'):
    dotenv_path = join(dirname(__file__), 'config.env')
    load_dotenv(dotenv_path)

# Get environment variables for Amazon AWS Access Keys


access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Create an S3 client

s3 = boto3.client(
   "s3",
   aws_access_key_id = access_key_id, 
   aws_secret_access_key = secret_access_key
)

# Print out available buckets

response = s3.list_buckets()
#print(response)


# Print each bucket name
