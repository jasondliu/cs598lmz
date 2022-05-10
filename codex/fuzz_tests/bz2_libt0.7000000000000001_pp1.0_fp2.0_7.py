import bz2
bz2.decompress(archive)

# сохраняем результат в файл
with open("vectors.bin", "wb") as out_file:
    out_file.write(archive)

print("Готово")

# Загружаем вектора
print("Загружаем вектора")

with open("vectors.bin", "rb") as in_file:
    archive = in_file.read()

zip_file = bz2.BZ2File(archive)

with open("vectors.bin", "wb") as out_file:
    out_file.write(zip_file.read())

print("Готово")
