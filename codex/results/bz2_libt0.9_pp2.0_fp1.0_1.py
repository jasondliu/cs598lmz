import bz2
bz2_compressor = bz2.BZ2Compressor()

def get_optimal_order(data):
    data = [(line[0], int(line[1:])) for line in data.split()]
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    return ''.join([str(x[1]) + x[0] for x in sorted_data])

if __name__ == '__main__':
    input_data = read_input_data('input.txt')
    if isinstance(input_data, str):
        input_data = input_data.encode('ascii')
    print('Decompressed length:', get_decompressed_length(input_data))
    # print('Length after recursion:', get_decompressed_length_recursive(input_data))
    print('Length after optimization:', get_length_after_optimization(bz2_compressor, input_data))
