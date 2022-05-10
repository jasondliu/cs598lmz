import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import Qt

from qutepart import Qutepart

app = QtWidgets.QApplication(sys.argv)

text = """
#include <stdio.h>

int main(int argc, char* argv[]) {
    int a = 0;
    printf("hello, world\\n");
    return 0;
}
"""

qpart = Qutepart()
qpart.text = text
qpart.setLanguage('C')
qpart.theme.baseColor = 'white'
qpart.theme.backgroundColor = 'white'
qpart.theme.selectionColor = '#F0F0F0'
qpart.theme.selectedTextColor = 'black'

qpart.res
