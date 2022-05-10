import io
class File(io.RawIOBase):
    def read(self,n):
        return "A"*n
    def write(self,data):
        pass
f=File()
f.read(10)
f.write("Hello")
 
io.RawIOBase
import docx
 
doc = docx.Document()
doc.add_picture('mario.png',width=docx.shared.Inches(1),height=docx.shared.Cm(4))
 
doc.save('hello.docx')
 
import docx2txt
 
text = docx2txt.process("hello.docx")
print(len(text))
print(text)
import requests, time
from bs4 import BeautifulSoup
 
url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
 
for page in range(0,30,10):
    r = requests.get(url+str(page)+".html", headers={'User-agent': 'Mozilla/5.0 (
