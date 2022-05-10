from lzma import LZMADecompressor
LZMADecompressor().decompress(open("cubes.lzma","rb").read()).decode("utf-8")

def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)

def nth_root_of_a_b(a,b,n):
    return nth_root(a,n) + nth_root(b,n)

def nth_root_of_a_plus_b(a,b,n):
    return nth_root(a+b,n)

def nth_root_of_a_minus_b(a,b,n):
    return nth_root(a-b,n)

def nth_root_of_a_times_b(a,b,n):
    return nth_root(a*b,n)

def nth_root_of_a_divided_by_b(a,b,n):
    return nth_root
