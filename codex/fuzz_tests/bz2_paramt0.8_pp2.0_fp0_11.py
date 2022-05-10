from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(file_content)
</code>
Salvo l'errore
<code>bz2.error: Error -3 while decompressing data: incorrect data check
</code>


A:

Essendo uno script Python è sufficiente risolvere il problema indicato, ovvero la mancanza della riga:
<code>#!/usr/bin/env python
</code>
nella prima riga del file <code>update.py</code>, ma in questo caso non è necessario neanche leggere lo script (che quindi non è disponibile nel file)
come ha detto @alexis, tar -xf update.py è la cosa giusta da fare.

