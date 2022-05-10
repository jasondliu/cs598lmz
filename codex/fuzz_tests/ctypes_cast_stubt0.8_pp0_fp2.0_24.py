import ctypes
ctypes.cast(my_device.models[0].m_handle, ctypes.py_object).value
ctypes.cast(my_device.models[1].m_handle, ctypes.py_object).value


import ctypes
ctypes.cast(my_device.network_descriptors[0].m_handle, ctypes.py_object).value
ctypes.cast(my_device.network_descriptors[1].m_handle, ctypes.py_object).value


import ctypes
ctypes.cast(my_device.operations[0].m_handle, ctypes.py_object).value
ctypes.cast(my_device.operations[1].m_handle, ctypes.py_object).value


import ctypes
ctypes.cast(my_device.tensors[0].m_handle, ctypes.py_object).value
ctypes.cast(my_device.tensors[1].m_handle, ctypes.py_object).value


import ctypes
ctypes.cast(my_device.tensor_views[0].m_
