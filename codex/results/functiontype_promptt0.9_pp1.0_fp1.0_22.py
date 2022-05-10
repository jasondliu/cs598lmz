import types
# Test types.FunctionType against the queued callback to test if the callback
# is a wrapper.
if isinstance(shared_var.get_then_del_queue(0).pop(), types.FunctionType):
    real_callback = shared_var.get_then_del_queue(0).pop()
    _ = real_callback()
    _ = shared_var.get_then_del_res(0).pop()
    real_callback = shared_var.get_then_del_queue(0).pop()
    _ = real_callback()
    _ = shared_var.get_then_del_res(0).pop()

    print('Pass!')
else:
    print('Fail!')
 
if __name__ == "__main__":
    pass

 
# Worker 1:
import shared_var
callback = lambda: shared_var.wrap_func(lambda : print('Hello from ', get_worker_id()))
send_notification(callback)# Won't be processed.

if __name__ == "__main__":
    pass

 
# Worker 2:
from __future__
