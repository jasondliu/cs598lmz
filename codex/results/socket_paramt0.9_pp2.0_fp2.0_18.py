import socket
socket.if_indextoname(2)
'b'en0''
>>>
```

Obtenir l'interface du routeur en utilisant **getroute**(af=10 AF_INET6) pour l'ipv6

```
>>> getroute(16) # on obtient à chaque fois la meme IP: ce sera le routeur
('2607:f8b0:400b:801::1003', '2600:3c03::f03c:91ff:fe98:7937', 2)
>>>
```

Obtenir la liste des IPV6 

```
>>> getnode(16) #on va obtenir la "node" (façon de dire le pc portable, c'est l'identifiant de ce dernier
[('b''en0''',2607:f8b0:400b:801::1004,2,2),('b'lo0',fe80::1,1,2)]
>>>
```


## ping

Pour faire du ping, on utilise le module **subprocess** donc
