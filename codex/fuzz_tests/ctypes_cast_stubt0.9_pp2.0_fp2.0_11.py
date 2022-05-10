import ctypes
ctypes.cast(objects.data, ctypes.py_object)

tr = objects.data[0].astype(float)
bl = objects.data[1].astype(float)
width = objects.data[2].astype(float)
height = objects.data[3].astype(float)

lista_out = [tr,bl,width,height]

tamanhos_caixas = (lista_out)


boxes = []
if not len(tamanhos_caixas):
    print("Nenhum objeto encontrado.")
else:
    for x in tamanhos_caixas:
        boxes.append((x[1],x[0],x[1]+x[3],x[0]+x[2]))

faces = []

croped_img = []

print (boxes)

for (startX, startY, endX, endY) in boxes:
    cv2.rectangle(img, (startX, startY), (endX, endY), (0, 0, 255), 2)

