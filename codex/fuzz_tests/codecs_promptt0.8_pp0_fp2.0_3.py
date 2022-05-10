import codecs
# Test codecs.register_error('strict_decode'

def main():
    # string = '문자열'
    # print(string)
    # binary_data = string.encode()
    # print(binary_data)
    # string = binary_data.decode('utf-8', 'strict')
    # print(string)

    f = open('hello.txt', 'w')
    f.write('Hello, world!')
    f.close()

    f = codecs.open('hello.txt', 'r', 'utf-8')
    u = f.read()
    f.close()

    f = open('hello.txt', 'rb')
    b = f.read()
    f.close()

    f = open('hello.txt', 'rb')
    b = f.read()
    f.close()

    f = open('hello.txt', 'rb')
    b = f.read()
    f.close()

    f = open('hello.txt', 'rb')
    b = f.read()
    f.close
