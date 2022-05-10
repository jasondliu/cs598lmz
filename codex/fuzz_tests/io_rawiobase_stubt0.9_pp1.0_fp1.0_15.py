import io
class File(io.RawIOBase):
    def readinto(self, b):
        n = len(b)
        s = self.read(n)
        n = len(s)
        try:
            b[:n] = s
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', s)
        return n

with open(os.path.join(sources_dir,'stdint.h'),'r') as stdint_h,open(os.path.join(sources_dir,'stdint.py'),'w')as stdint_py:
    stdint_py.write(parseStdint(stdint_h))
    stdint_py.write('\n_intN_types = (\n')
    for intN_type,_ in _intN_types:
        stdint_py.write('    {}.{},\n'.format(intN_type.module,intN_type.__name__))
    stdint_py.write
