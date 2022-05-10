import lzma
# Test LZMADecompressor
TestLZMA = False
if TestLZMA:
    from functools import partial
    from io import BytesIO
    from itertools import repeat, chain
    
    from tqdm import tqdm
    from lzma import LZMADecompressor
    from lzma import FORMAT_XZ
    
    #from multiprocessing.pool import Pool
    import multiprocessing as mp
    
    #from multiprocessing.pool import ThreadPool
    import multiprocessing.dummy as mpd
    mp_map = mpd.Pool().map
    
    import os
    if os.name == "nt":
        print("Set the multiprocessing context to spawn")
        mp.set_start_method("spawn")
    
    if __name__ == "__main__":
        
        N = int(1e8)
        #N = int(1e1)
        datasize = int(N * 4)
    
        #data = np.frombuffer(np.random.bytes(datasize), dtype=
