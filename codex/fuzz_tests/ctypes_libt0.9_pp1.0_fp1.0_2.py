import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("pysimplemu")

#create console and window instances
window = pysimplegui.window("pysimplemu")
console = window.console

#populate menu with items you want available
mt_type = ["text", "text", "text", "text", "text"]
mt_name = ["X", "Y", "Z", "NEW 1", "NEW 2"]
mt_key = ["Key A", "Key =", "Key S", "Key Up", "Key Left"]
#mt_id = ["m1", "m2", "m3", "m4", "m5"]
mt_items = [[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]

#set menu items
window.set_menu_data(mt_type, mt_name, mt_items, mt_key)

event, values = window.Read()

#create your timer
