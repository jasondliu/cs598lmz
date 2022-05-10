import io
# Test io.RawIOBase to read and write the file.

# Example 1:
# Write string to a file:
f = open('C:/Users/Renata/Desktop/Day 4/write.txt', 'w')
f.write('This is a test\n')
f.close()

print(open('C:/Users/Renata/Desktop/Day 4/write.txt', 'r').read())

# Example 2:
# Write lines to a file:
f = open('C:/Users/Renata/Desktop/Day 4/write.txt', 'w')
f.writelines(['This is a test\n', 'Hello world\n'])
f.close()


# Example 3:
# Write tuple to a file:
f = open('C:/Users/Renata/Desktop/Day 4/write.txt', 'w')
f.writelines(('test1', 'test2'))
f.close()



# Example 4:
# Write dictionary to a file:
f = open('C:/Users/Renata/Desktop/Day 4/write.txt', 'w')
f.writelines
