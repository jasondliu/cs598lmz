import sys, threading

def run():
    account_name = "admin"
    account_key = "0bUjK3qMkSXv/CzD5K/2Qx5bW4+GwN/N/fHhA/eLW8fvU6L0n6RocGcxmW8gn2IYlDmBBnq3m7sW9CQcKiAG3Q=="
    container_name = "test"
    blob_name = "test.txt"

    try:
        print("Azure Blob storage v12 - Python quickstart sample")
        # Quick start code goes here
        # Create the BlobServiceClient object which will be used to create a container client
        blob_service_client = BlobServiceClient.from_connection_string(
            conn_str="DefaultEndpointsProtocol=https;AccountName=" + account_name + ";AccountKey=" + account_key + ";EndpointSuffix=core.windows.net")

        # Create a file in local Documents directory to upload and download
        local_path = os.path
