import weakref

def permute_list(list, num_shuffles):
    for i_shuffle in range(num_shuffles):
        idx = randint(0, len(list)-1)
        tmp = list[idx]
        list[idx] = list[0]
        list[0] = tmp
    return list

def tuple_to_str(tup):
    return ''.join(str(t) for t in tup)

def select_without_replacement(list, num_items):
    """This method is quite buggy, and would supossedly give a uniform distribution of the selected indexes, but it does not, who knows why... so we are back to Fisher-Yates"""

    #assert(num_items <= len(list))
    #if num_items > len(list):
        #num_items = len(list)
    #list_to_return = []
    #for i in range(num_items):
        #idx = randint(0, len(list)-1)
        #list_to_return.append(id
