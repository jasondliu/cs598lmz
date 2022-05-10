import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print "Function called."
    return '21'

def destroy(widget, event, data=None):
    gtk.main_quit()

if __name__ == '__main__':
    window = gtk.Window()
    window.connect("destroy", destroy)
    window.set_border_width(1)
    window.show()
    
    #model = gtk.ListStore(FUNTYPE)
    model = gtk.ListStore(ctypes.py_object)
    it = model.append([fun])
    
    col = gtk.TreeViewColumn('Functions')
    
    
    renderer = gtk.CellRendererText()
    col.pack_start(renderer)
    #col.add_attribute(renderer, 'text', 0)
    col.set_cell_data_func(renderer, fun)
    #col.set_attributes(renderer, text=1)
    
    view = gtk.TreeView(model)
    view.show()
    view.append_column(col)
    

