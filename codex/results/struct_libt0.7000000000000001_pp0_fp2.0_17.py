import _struct
import _struct as struct

def Get_Set_Value( item,  value = None):
	if value == None:
		return item.get()
	else:
		item.set(value)

def Get_Set_Value_Entry( item,  value = None):
	if value == None:
		return item.get()
	else:
		item.delete(0, END)
		item.insert(0, value)

def Get_Set_Value_Combobox( item,  value = None):
	if value == None:
		return item.get()
	else:
		item.set(value)

def Get_Set_Value_Spinbox( item,  value = None):
	if value == None:
		return item.get()
	else:
		item.delete(0, END)
		item.insert(0, value)


class tk_Frame(Frame):
	def __init__(self, master, width = -1, height = -1, pack = False, bd
