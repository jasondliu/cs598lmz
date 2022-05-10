import socket
socket.if_indextoname()
#conv_interface('10.3.1.1')

# def remove_duplicate(lst):
#     rtn = []
#     for x in lst:
#         if x not in rtn:
#             rtn.append(x)
#     return rtn
#
#
# def sort_dict(a_dict):
#     return sorted(a_dict.items(), key=lambda x: x[1])
#
#
# def get_threshold(item):
#     if type(item) == dict:
#         item = remove_duplicate(list(item.keys()))
#     sort_list = sort_dict(item)
#     l_val, l_key = sort_list[-1]
#     r_val, r_key = sort_list[-2]
#     return (l_val - r_val) / 4 + r_val
#
#
# for key in csfa_dict:
#     data = csfa_dict[key]
#     item = []
#     for vector in data
