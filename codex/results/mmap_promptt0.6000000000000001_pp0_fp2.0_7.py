import mmap
# Test mmap.mmap.find
m = mmap.mmap(0, 1, "test_mmap_find")
m.write("abcdefghijk")
m.seek(0)
assert m.find("def") == 3
assert m.find("fg") == -1
assert m.find("i") == 9
assert m.find("j") == 10
assert m.find("abc") == 0
assert m.find("ghi") == 6
assert m.find("def", 4) == -1
assert m.find("def", 3) == 3
assert m.find("def", 3, 6) == -1
assert m.find("", 3) == 3
assert m.find("", 3, 6) == -1
assert m.find("", 3, 6, 2) == -1
assert m.find("", 3, 6, 4) == 3
assert m.find("", 3, 6, 5) == 3
assert m.find("", 3, 6, 6) == -1
assert m.find("", 1, 1) == -1
assert m.find("", 0, 0) ==
