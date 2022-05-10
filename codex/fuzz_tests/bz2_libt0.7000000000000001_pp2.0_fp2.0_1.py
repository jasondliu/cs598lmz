import bz2
bz2_file = bz2.BZ2File("/home/repo/develop/notebooks/data/compression/wikipedia.txt.bz2")
print(bz2_file.readline())

print(bz2_file.readline().decode('utf-8'))

# %% [markdown]
# ## gzip
# %% [markdown]
#
# gzipは、deflate圧縮を用いてデータを圧縮する。
#
# gzipは、１つのデータを圧縮するので、１つのファイルに対して１回しか書き込めない。
#
# ファイルを圧縮すると同時にテキスト形式でも保存することができる。
#
# gzipは、ファイル圧縮に特化している。
#
