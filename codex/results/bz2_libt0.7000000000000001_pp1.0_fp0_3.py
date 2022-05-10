import bz2
bz2.decompress(response.content) 

# to store the decompressed data in a file
bz2.decompress(response.content, open("data.xml", "wb"))

# to store the decompressed data in a file
open("data.xml", "wb").write(bz2.decompress(response.content))

# to store the decompressed data in a file
open("data.xml", "wb").write(
    bz2.decompress(
        urllib.request.urlopen("http://daten.berlin.de/datensaetze/stadtentwicklungsplanung-berlin-bis-2030-makrozellen-gesamtplan-kommentiert/metadaten/data.xml.bz2").read()
    )
)

# to print the decompressed data
print(bz2.decompress(
    urllib.request.urlopen("http://daten.berlin.de/datensaetze/stadtentwicklungsplanung-berlin-bis-
