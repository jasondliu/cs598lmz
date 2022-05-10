import codecs
# Test codecs.register_error() here

decoder_map = codecs.make_identity_dict(range(256))
encoder_map = codecs.make_encoding_map(decoder_map)

def binary_search(collection, target):
    left = 0
    right = len(collection) - 1

    while left <= right:
        midpoint = (left + right) // 2
        current_item = collection[midpoint]
        if current_item == target:
            return midpoint
        else:
            if target < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
    return None

def binary_recursive(collection, target):
    if len(collection) == 0:
        return None
    else:
        midpoint = len(collection) // 2

        if collection[midpoint] == target:
            return midpoint
        else:
            if collection[midpoint] < target:
                return binary_search(collection[midpoint + 1:], target)
