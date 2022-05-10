import lzma
lzma_version = tuple([int(x) for x in lzma.__version__.split(".")])
requires_lzma_835 = pygsti_version >= (0.9, 9, 0) and lzma_version >= (0, 8, 35)

def main():
    import gzip
    with gzip.open('dataset.dataset.obj.gz', 'rb') as f:
        load(f)
       

if __name__ == "__main__":
    main()
