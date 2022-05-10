import threading
threading.stack_size(67108864)

# Identify the data directory
data_dir = './data'

# Define the categories
categories = ["dogs", "cats"]

# Iterate through each category
for category in categories:  
    
    # Create a folder for that category
    os.makedirs(os.path.join(data_dir, category), exist_ok=True)

def download_single_img(url, dest):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(dest, 'wb') as f:
            for chunk in r:
                f.write(chunk)

def download_images(query, output_dir, num_images):
    # API key and CX are stored in a separate file not uploaded to GitHub
    api_key, cx = get_credentials()
    # API key and CX are stored in a separate file not uploaded to GitHub
    
    # Build the URL
    query = "+".join(query.split())
    url = "
