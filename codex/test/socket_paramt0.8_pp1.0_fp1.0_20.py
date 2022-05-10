import socket
socket.if_indextoname('eth0')

DataBase = {
    'IP': '127.0.0.1',
    'PORT': '1433',
    'USER': 'sa',
    'PASSWORD': 'fuxu!123',
    'DB': 'Voucher', }

BaseUrl = {
    'URL': '',
    'REST_Header': {
        'Authorization': 'token',
        'Content-Type': 'application/json',
    }
}

PayOrder = {
    'OrderID': '',
    'Amount': '',
    'Paid': '',
    'PayStatus': '',
}

