import codecs
codecs.register_error(
    'myRepl', 
    codecs.replace_errors)

download_path = argv[2]

def download(url):
    pbar = tqdm(total=100)
    with open(download_path, 'wb') as f:
        response = requests.get(url, stream=True)
        total_length = response.headers.get('content-length')
    
        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                pbar.update(done)
                pbar.write(str(done) + "%")
    pbar.close()

def main():
    parser = argparse.ArgumentParser(description='Download file')
    parser.add_argument('-u', '--
