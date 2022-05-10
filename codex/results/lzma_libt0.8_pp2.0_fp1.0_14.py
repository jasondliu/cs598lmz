import lzma
lzma.decompress("".join(list(filter(lambda x: x.strip() != "", open("download_links/linux.lzma").read().split("\n"))))).decode("utf-8")

def download_files(files):
  """
  downloads files from the list of strings, should run in parallel
  """
  for file in files:
    try:
      response = requests.get(file.strip(), stream=True)
      if response.status_code == 200:
        open("data/" + file.split("/")[-1], "wb").write(response.raw.read())
    except:
      print("Error downloading file", file)

def uncompress_files(files):
  """
  uncompress lzma file in parallel
  """
  for file in files:
    if file.endswith(".lzma"):
      try:
        open("data/" + file.split("/")[-1][:-5] + ".json", "wb").write(lzma.decompress("".join(list(filter
