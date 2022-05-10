import mmap
# Test mmap.mmap
map_file = mmap.mmap(fileno=open("test.txt").fileno(), length=1024, flags=mmap.MAP_INHERIT, prot=mmap.PROT_WRITE)
map_file.resize(1024*1024)
map_file.write("test")


JSON_OBJECT = """
{
	"key":"value",
	"value":100,
	"array":[1,2,3,4,5],
	"obj":{
		"key1":"val1",
		"key2":[6,7,8,9,10]
	}
}
"""

JSON_ARRAY = """
[
	"val1",
	"val2",
	"val3",
	"val4",
	"val5"
]
"""
str1 = r'\/test/test2/tet12'
str2 = r'/test/test2/tet12'
if str1 == str2:
	print("hello")
	pass
else:
	print("world")
	pass


