fn = lambda: None
# Test fn.__code__
with pytest.raises(TypeError):
    fn.__code__ = 1
with pytest.raises(TypeError):
    fn.__code__ = float('nan')
with pytest.raises(TypeError):
    fn.__code__ = 'A'

# Test fn.__closure__
with pytest.raises(TypeError):
    fn.__closure__ = 1
with pytest.raises(TypeError):
    fn.__closure__ = float('nan')
with pytest.raises(TypeError):
    fn.__closure__ = 'A'
with pytest.raises(TypeError):
    fn.__closure__ = (1,)
with pytest.raises(TypeError):
    fn.__closure__ = (float('nan'),)
with pytest.raises(TypeError):
    fn.__closure__ = ('A',)
with pytest.raises(TypeError):
    fn.__closure__ = (float('nan'), 1, 'A')

# Test fn.__defaults__
with pytest.raises
