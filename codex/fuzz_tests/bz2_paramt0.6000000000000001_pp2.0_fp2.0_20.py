from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# найдем индекс первого символа нашего контента
start = data.find(b'<div id="mw-content-text"')
# и найдем индекс начала следующего тега с закрывающим слешем
end = data.find(b'<div class="printfooter"')
# вырежем все, что между ними
data = data[start:end]

# подготовим простой регулярный выражен
