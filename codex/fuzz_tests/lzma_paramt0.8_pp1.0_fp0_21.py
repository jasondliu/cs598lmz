from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed).decode("utf-8").strip()

#%%
import multiprocessing as mp

def f(x, y):
    print (x, y)
    return x+y

if __name__ == '__main__':
    with mp.Pool(5) as p:
        print(p.map(f, [1, 2, 3], [4, 5, 6]))
#%%

def f(x, y):
    print (x, y)
    return x+y

if __name__ == '__main__':
    pool = mp.Pool(5)              # start 4 worker processes
    result = pool.apply_async(f, [10, 20])    # evaluate "f(10)" asynchronously
    print(result.get(timeout=1))           # prints "100" unless your computer is *very* slow
    print(pool.map(f, range(10)))          # prints "[0, 1, 4,..., 81]"
    it = pool.imap(f, range(10))
    print(
