import io
# Test io.RawIOBase class
# ...
class Flux(io.RawIOBase):
    def __init__(self, flux, taille):
        self.flux = flux
        self.taille = taille
        self.curseur = 0

    def read(self, taille):
        data = self.flux[self.curseur:(self.curseur + taille)]
        self.curseur += taille
        return data
# ...
flux = Flux(b"azerty", 6)
flux.read(2)

# Out[]: b'az'

flux.read(2)

# Out[]: b'er'

while True:
    data = flux.read(10)
    if data == b'':
        break
    print(data)

# Out[]: b'ty'
# Test io.BufferedIOBase class
# ...
class Flux(io.BufferedIOBase):
    def __init__(self, flux, taille):
        self.flux = flux
        self.taille = taille
