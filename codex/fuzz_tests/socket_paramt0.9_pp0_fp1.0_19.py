import socket
socket.if_indextoname(65)

#install msftdiag and libftdi to debug
import msftdiag, tui
tui.dump(msftdiag.get().get_devices().data)

#used for pca to monitor all changes in data structure
# import msftdiag
# from pca import Document, Pca, View
# 
# view = View()
# pca = Pca(Document())
# pca.registerObserver(view.update)
# pca.run()
