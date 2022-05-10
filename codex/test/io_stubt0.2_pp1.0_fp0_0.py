import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)

# io.BufferedReader.readinto()
# io.BufferedReader.readinto1()
# io.BufferedReader.readinto2()
# io.BufferedReader.readinto3()
# io.BufferedReader.readinto4()
# io.BufferedReader.readinto5()
# io.BufferedReader.readinto6()
# io.BufferedReader.readinto7()
# io.BufferedReader.readinto8()
# io.BufferedReader.readinto9()
# io.BufferedReader.readinto10()
# io.BufferedReader.readinto11()
# io.BufferedReader.readinto12()
# io.BufferedReader.readinto13()
# io.BufferedReader.readinto14()
# io.BufferedReader.readinto15()
# io.BufferedReader.readinto16()
# io.BufferedReader.readinto17()
# io.BufferedReader.readinto18()
# io.BufferedReader.readinto19()
# io.BufferedReader.readinto
