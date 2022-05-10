import selectors
from retriever import fetch_images, get_image_from_instagram
from markup import InscriptionGenerator
from sys import stdin
import json


def main():
    if len(sys.argv) < 3:
        print('Usage: python3 %s <search> <file1>,<file2>,...' % sys.argv[0])
        sys.exit(1)
    search = sys.argv[1]
    files = []

    for word in sys.argv[2].split(','):
        files.append(FetchFile(word.strip(), search))

    loop = asyncio.get_event_loop()
    fetch_coro = asyncio.wait([f.fetch() for f in files])
    loop.run_until_complete(fetch_coro)
    loop.close()
    print(json.dumps([file.token for file in files]))



