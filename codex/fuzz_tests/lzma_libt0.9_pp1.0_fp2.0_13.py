import lzma
lzma.open = lzma.LZMAFile

msun = 1.9889e30  # kg
g = 9.80665  # m/s^2
c = 299792458. # m/s
h = 6.62607e-34 # m^2 kg / s
kB = 1.38065e-23 # m^2 kg s^-2 K^-1
year = 3.15576e7 # s

day = 60**2*24 # s
hour = 60**2 # s

class collapse(object):

    def __init__(self,inifileName='ini.ini'):

        self.name = None

        self.inifileName = inifileName

        self.datafileName = None
        self.datafile = None

        self.numbersFileName = None
        self.numbersFile = None

        self.figureDir = None

        self.starProbability = None
        self.starmass = None
        self.starRadius = None

        self.saveTime = None
        self.tmax =
