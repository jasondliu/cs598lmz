import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()
from IPython.display import Image, display
display(Image(url='https://raw.githubusercontent.com/fjvarasc/DSPXI/master/figures/logo.png'))

x = np.arange(0, 2 * np.pi, 0.3);
