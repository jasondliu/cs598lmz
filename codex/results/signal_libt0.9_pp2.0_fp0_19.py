import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
def _delete_frame(frame):
    frame.lbl_autoPIL.config(text="AutoPIL: %s"%var_autostore.get())
    frame.currenttool=""
    frame.update()
    DelWin(root,frame)
    if frame.widgetlist != []:
        "del all the widget"
        del frame.widgetlist[:]
    frame.destroy()
    
def _get_frame(framenames):
    b=bk.obj_dict[framenames]
    return b

def _delete_wid(widget):
    widget.grid_forget()

def update_VariVar(frame):
    var1=eval(frame.var_list[0].get())
    var2=eval(frame.var_list[1].get())
    var3=eval(frame.var_list[2].get())
    var4=eval(frame.var_list[3].get())
    frame.var=Update_VarVar(var
