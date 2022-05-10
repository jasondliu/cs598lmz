import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

with open("../data/input_file.txt") as f:
    data = f.read()

print(data)

with open("../data/output_file.txt", "w") as f:
    f.write(data)
