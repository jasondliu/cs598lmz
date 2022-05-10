import lzma
lzma.LZMADecompressor().decompress(open("regex_compressed.txt.xz", "rb").read())
</code>
I got this error:
<code>ValueError: Incorrect input data
</code>
I am using python 3.7.3, this is my environment
<code>Name                    Version                   Build  Channel
_libgcc_mutex            0.1                        main  
_openmp_mutex            4.0                        main  
attrs                    19.1.0                     py_0  
blas                     1.0                         mkl  
ca-certificates          2019.3.9                 hecc5488_0    conda-forge
certifi                  2019.3.9                 py37_0  
cffi                     1.12.3           py37hb5b8e2f_0    conda-forge
chardet                  3.0.4                 py37_1003  conda-forge
click                    7.0                      py37_0  
cryptography             2.7              py37h1ba5d50_0   
