from lzma import LZMADecompressor
LZMADecompressor()

from lxml import html
import requests

page =requests.get('http://127.0.0.1:8000/pFormula/index.html')
tree=html.fromstring(page.content)

</code>
If it worked, you would see a page like this:

Because the data you are trying to access is dynamic, you need a web browser that supports JavaScript.
If you are using a real browser, then your code should find the form like this:
<code>inputs = tree.xpath('//*[@id="edit-input"]')
inputs[0].value = 13.6

inputs = tree.xpath('//*[@id="edit-input-2"]')
inputs[0].value = 0.27

inputs = tree.xpath('//*[@id="edit-submit"]')
inputs[0].click()
</code>
Which will solve your problem.
But if you are using any python module, then maybe you can write a crawler for a website with a small amount of data, but for a website that is dynamic and has
