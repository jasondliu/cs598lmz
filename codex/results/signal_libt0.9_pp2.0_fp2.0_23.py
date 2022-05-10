import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

#matplotlib config
#mpl.rcParams['legend.numpoints'] = 1 #default 2dots
#mpl.rcParams.update({'font.size': 12})
#mpl.rcParams['xtick.labelsize'] = 20
#mpl.rcParams['ytick.labelsize'] = 20

##
def runme():
     pass





## THIS BIT IS FROM: http://graal.ift.uni.wroc.pl/~ludwik/python/matplotlib/iva_toolkit/matplotlib_toolkit.py
## but was customized a litttle bit
def mkscatter(ax = None,
      x = [1,2,3], #x data
      y = [1,1,1], #ydata
      **kwargs):


   if ax is None: ax = plt.gca()

   x = numpy.array(x)
   y = numpy.array(y
