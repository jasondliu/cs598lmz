import ctypes
ctypes.cast(0, ctypes.c_void_p)

#%%
import pyvisa
rm = pyvisa.ResourceManager()
device_list = rm.list_resources()
print(device_list)
#%%
from pyvisa.constants import StatusCode
instr = rm.open_resource(device_list[0])#resource_name
print(instr.query("*IDN?"))
instr.write("INST:SEL P25V")
print(instr.query("INST:SEL?"))
#%%
print(instr.query("INST:SEL?"))
instr.write("INST:SEL P25V")
instr.write("MEAS:CURR:DC?")
print(instr.read())
instr.write("MEAS:VOLT:DC?")
print(instr.read())
#%%
instr.write("INST:SEL P6V")
instr.write("CURR 1")#mA
instr.write("OUTP ON")
instr.write("MEAS:CURR:DC?")

