import threading
threading.Thread(target=add_to_list).start()

#[2, 1]
print(my_list)
</code>
If your <code>add_to_list</code> function is doing something simple, you can just use <code>append</code> instead of <code>extend</code>.
<code>my_list.append(new_item)
</code>

