import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, GtkWidget_p, gpointer, gpointer)
REV_TREE_MOVE_FUNC = FUNTYPE(reverse_tree_model_drag_drop)
sort_order_types.set(HISTORY, 'type', 'search_text', 'date_decreasing')

def _history_add(path, typ, val):
    row = GtkListStore()
    if not sort_order_types.add(HISTORY, path, row, typ, val):
        return
    path = row.get_path()
    row_itr = sort_order_types[HISTORY].get_iter(path)
    row.set_value(row_itr, 0, path)
    row.set_value(row_itr, 1, val)
    row.set_value(row_itr, 2, typ)
    sort_order_types[HISTORY].row_changed(path, row_itr)
    return path

def _history_get(path):
    row = sort_order_types[HISTORY]

