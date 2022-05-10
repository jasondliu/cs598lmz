import ctypes
ctypes.cast(work_items, ctypes.py_object), #work_items is a list of work_item objects
</code>
and then:
<code>def PrintValue(work_item):
    print(work_item._val)

def UpdateValue(work_item):
    work_item._val = work_item._val * 10

def UpdateValues(row, work_items): #work_items is the list passed by my foreach
    [UpdateValue(work_item) for work_item in work_items]

def PrintValues(row, work_items):
    [PrintValue(work_item) for work_item in work_items]

pool.map(UpdateValues, rows)
pool.map(PrintValues, rows)
</code>

