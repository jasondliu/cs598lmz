import bz2
# Test BZ2Decompressor
# bz_file = bz2.BZ2File(filename)
# data = bz_file.read()
# bz_file.close()
# raw_data = bz2.decompress(data)
# def download_and_extract_dataset(dataset_name: str, output_dir: str):
#     if not os.path.isdir(output_dir):
#         os.makedirs(output_dir)
#     url = DATASET_URLS[dataset_name]
#     filename = url.split('/')[-1]
#     if not os.path.exists(output_dir + '/' + filename):
#         def _progress(count, block_size, total_size):
#             sys.stdout.write('\rDownloading %s %.2f%%' % (
#                 filename, float(count * block_size) / float(total_size) * 100.0))
#             sys.stdout.flush()
#         urllib.request.urlretrieve(url
