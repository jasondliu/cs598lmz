import codecs
codecs.register_error('strict', codecs.ignore_errors)


def download_single_file(url, dest_dir):
    try:
        response = requests.get(url, allow_redirects=True)
        with open(dest_dir, 'wb') as f:
            f.write(response.content)
            return True
    except Exception as e:
        return False


def download_single_file2(url, dest_dir):
    try:
        response = requests.get(url, allow_redirects=True)
        with codecs.open(dest_dir, 'wb', 'utf-8', 'strict') as f:
            f.write(response.content)
            return True
    except Exception as e:
        return False


def download_mp3_files(url_list, dest_dir):
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    pbar = tqdm(url_list)
    for url in pbar:
        pbar.set_description(url)

