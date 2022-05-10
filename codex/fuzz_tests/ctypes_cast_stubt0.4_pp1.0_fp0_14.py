import ctypes
ctypes.cast(a, ctypes.py_object).value

#%%

def get_mask(mask, shape):
    mask = np.array(mask)
    if mask.shape[0] == shape[0]:
        return mask
    else:
        return mask.T

def get_mask_from_list(mask_list, shape):
    if len(mask_list) == 1:
        mask = mask_list[0]
        return get_mask(mask, shape)
    else:
        mask = np.zeros(shape)
        for m in mask_list:
            mask = mask + get_mask(m, shape)
        return mask

def get_mask_from_list_of_list(mask_list_of_list, shape):
    mask = np.zeros(shape)
    for mask_list in mask_list_of_list:
        mask = mask + get_mask_from_list(mask_list, shape)
    return mask

def get_mask_from_list_of_list_of_list(mask_list_of_
