import socket
socket.if_indextoname(3)

>>> socket.if_indextoname(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: [Errno 22] Invalid argument
```

[これ](https://stackoverflow.com/questions/7337887/address-already-in-use-while-listening-on-uDP)を参考にすると、`setsockopt`関数でソケットオプションを設定することで、タイムアウト付きで待機できます。

また、[こちらも](https://stackoverflow.com/questions/39192325/error-address-already-in-use-while-doing-udp-broadcast)参考にしたところ、OS内で再利用する間隔を短くすることでも解消できるよう
