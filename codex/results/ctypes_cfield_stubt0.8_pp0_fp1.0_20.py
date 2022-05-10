import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
</code>
I'm trying to use ipywidgets to create a custom IntSlider widget that also displays the hexadecimal value. I want to set the underlying ctypes object to the value that the user clicks. I found the answer to a similar question at How to manipulate values of ctypes arrays with numpy? but it appears that Jupyter does not support modifying ctypes objects.
<code>import ctypes
import ipywidgets as widgets

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s = S()

def set_val(v):
    #s.x = v.new
    s.x = v['new']
    print(hex(s.x))

int_slider = widgets.IntSlider(min=0,max=0xffffffff,step=1,value=0,description='Value')
int_slider.observe(set_val, names='value')
display(int_slider)


print(hex(s.x))
print(type(int_slider
