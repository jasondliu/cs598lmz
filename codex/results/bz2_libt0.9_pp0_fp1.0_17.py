import bz2
bz2.decompress(data)

# Exceptions & Graceful Errors
# http://localhost/hello
my_dict = { "name": "Anna" }
my_dict["address"]  # => KeyError: 'address'

# Introduce nested dictionary helper method
def get_from_dict(data_dic, comp_list ):
    return reduce(lambda d, k: d[k], comp_list, data_dic)

my_dict = { "name": "Anna" }
get_from_dict(my_dict, "name") # => "Anna"
my_dict["address"] # => KeyError: 'address'
get_from_dict(my_dict, ["address", "zipcode"]) # => KeyError: 'address'
get_from_dict(my_dict, ["name", "address", "zipcode"]) # => KeyError: 'address'

address = {
    "street": "USC",
    "city": "Los Angeles"
}
my_dict["address"] = address
get_from_dict(my_dict, ["name", "
