import socket
socket.if_indextoname(7)

# In[12]:


import socket
socket.gethostbyaddr('127.0.0.1')

# In[1]:


from wsgiref.simple_server import make_server

def application (environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    return ['Hello world!']

httpd = make_server('', 8000, application)
print('Serving on port 8000...')
httpd.serve_forever()
