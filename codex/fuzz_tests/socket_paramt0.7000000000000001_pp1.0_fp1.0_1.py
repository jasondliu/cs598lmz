import socket
socket.if_indextoname(3)

socket.if_indextoname(3)
#'en7'

socket.gethostname()
#'jovyan-ubuntu'

socket.gethostbyname('jovyan-ubuntu')
#'172.17.0.2'

socket.gethostbyname_ex('jovyan-ubuntu')
#('jovyan-ubuntu', ['jovyan-ubuntu'], ['172.17.0.2'])

socket.gethostbyname_ex('jovyan-ubuntu')[2]
#['172.17.0.2']

socket.gethostbyname_ex('jovyan-ubuntu')[2][0]
#'172.17.0.2'

socket.gethostbyname_ex('jovyan-ubuntu')[2][0]
#'172.17.0.2'

socket.gethostbyname_ex('jovyan-ubuntu')[2][0]
#'172.17.0.2'

socket.gethostbyname_ex('jovyan-ubuntu')
