import codecs
# Test codecs.register_error to ignore certain Unicode Errors

# Build our own handler for UTF-8 errors
class MyUTF8Handler(codecs.UTF8Error):
  def __init__(self,msg,errors='ignore'):
    self.errors = errors
    self.msg = msg
  def handle(self,achar): return achar

codecs.register_error("MyUTF8", MyUTF8Handler)

u = u"\ufffdabcdef" # Should be ...abcdef
s = u.encode("utf8","MyUTF8")

print s

print codecs.encode(u.encode('utf8'), "MyUTF8")

print u"\ufffdabcdef".encode('utf8', 'MyUTF8')

print codecs.encode(u"\ufffdabcdef", "MyUTF8")
