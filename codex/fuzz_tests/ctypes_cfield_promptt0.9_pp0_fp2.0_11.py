import ctypes
# Test ctypes.CField is same as FieldInfo

def get_obj_fields(obj):
    """
    Returns" a dict of all fields in an object where:
     - the key is a string of the name of the field.
     - the value is a string of the value of the field.
     - If a field is of type list or dict, then repr() is called on
       it to convert it to a string.
    """
    num_fields = len(obj._fields_)
    # Create a blank list of the correct length.
    res = [None] * num_fields 
    for i in range(0, num_fields):
        # Get the field name and value
        field_name = obj._fields_[i][0]
        field_val = getattr(obj, field_name)
        if isinstance(field_val, list) or isinstance(field_val, dict):
            # Special handling for list or dict!
            res[i] = (field_name, repr(field_val))
        else:
            res[i] = (field_name, field_val)
   
