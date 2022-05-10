import ctypes
ctypes.cast(1, ctypes.c_void_p)

class renderstate_base_t(ctypes.Structure):
    _fields_ = [('cullMode', ctypes.c_uint), ('flags', ctypes.c_uint), ('shadowPassIndex', ctypes.c_int)]

renderstate_base_t.cullMode

s = str(renderstate_base_t)
s[s.index('{'):]

class renderstate_t(renderstate_base_t):
    classmembers = '''
        pass
    '''.split('\n')[1:-1]
    def __post_init__(self):
        '''
        print('FIXME {0}'.format(self.cullMode))
        for i in range(4):
            for j in range(4):
                print(self.bounds.value[i][j], end=' ')
            print()
        '''
        pass
        
    def __str__(self):
        return '''{0}
cullMode = {1}
flags = {
