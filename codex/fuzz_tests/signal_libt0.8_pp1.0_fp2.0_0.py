import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
# self._qapp.exit(0)
table = Table.read('/home/guido/Documents/Master/Stage/Dati/RDP/RDP_data.csv', delimiter=';', fill_values=('', np.nan))
table_paran = Table.read('/home/guido/Documents/Master/Stage/Dati/RDP/Paranal/Parameters.csv', delimiter=';', fill_values=('', np.nan))
# table_alma = Table.read('/home/guido/Documents/Master/Stage/Dati/RDP/ALMA/Parameters.csv', delimiter=';', fill_values=('', np.nan))
# table_sma = Table.read('/home/guido/Documents/Master/Stage/Dati/RDP/SMA/Parameters.csv', delimiter=';', fill_values=('', np.nan))
# table_apex = Table.read('/home/guido/Documents/Master/Stage/Dati
