from lzma import LZMADecompressor
LZMADecompressor().decompress(readFile("../data/user_agent_data.lzma"))
</code>
I'm expecting this to take around 1 minute to decompress. However, it takes around 3 minutes.
This is my exact code:
<code>import time

def readFile(filename):
    with open(filename, "rb") as file:
        return file.read()

def timeit(function):
    start_time = time.time()
    function()
    print("--- %s seconds ---" % (time.time() - start_time))

timeit(lambda: LZMADecompressor().decompress(readFile("../data/user_agent_data.lzma")))
</code>
I'm running this on a Macbook Pro (late 2016).
Am I doing something wrong?

