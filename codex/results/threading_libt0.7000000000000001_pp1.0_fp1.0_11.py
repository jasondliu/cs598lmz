import threading
threading.Thread(target=s.run, args=(), daemon=True).start()
 
# Test the browser
print('Opening browser')
b.get('http://www.duckduckgo.com')
 
# Test the fake display server
v.start_display()
w.start_display()
 
# Done
print('Press any key to close...')
input()
