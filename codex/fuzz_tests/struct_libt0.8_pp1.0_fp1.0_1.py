import _struct
import time
import os
import numpy as np
import types

def _get_field_names(datatype):
  """
  Extracts field names from a structured numpy ndarray.
  """
  datatype = _np.dtype(datatype)
  if len(datatype.fields) != 1:
    raise ValueError("Expecting a single field.")
  else:
    name, dtype = datatype.fields.items()[0]
    return name, dtype[0]

def _get_unpack_format(data):
  """
  Extracts unpack format from a structured numpy ndarray.
  """
  field_name, field_dtype = _get_field_names(data.dtype)
  return ">i" + field_name + _struct.pack("i", data.size)[1:]

def _extract_buffer(dtype, buffer, offset=0):
  """
  Extracts field from a structured numpy ndarray using offset.
  """
  field_name, field_
