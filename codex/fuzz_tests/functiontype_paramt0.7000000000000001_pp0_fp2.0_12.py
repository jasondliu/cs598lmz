from types import FunctionType
list(FunctionType(f, d)())

# (gdb) p *f
# $1 = {
#   _ob_next = 0x0, 
#   _ob_prev = 0x0, 
#   ob_refcnt = 1, 
#   ob_type = 0x7ffff7a1b240, 
#   ob_size = 0, 
#   ob_digit = {
#     0 <repeats 15 times>
#   }, 
#   ob_sval = {
#     ob_sval = "d\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000", '\000' <repeats 49 times>, "\037\000\000\000\000\000\000\000\000\000\000\000
