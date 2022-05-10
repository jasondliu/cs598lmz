from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(
    format='>HH',
    size=4
)
s.unpack(b'\x00\x01\x00\x02')
# (1, 2)
```

## 样本

* `server.py` 基于 `SocketServer` 模块的多线程 TCP 服务器
* `client.py` 多线程 TCP 客户端
* `protocol_v1.py` 简单的请求-响应协议
* `protocol_v2.py` 消息长度前缀协议
* `protocol_v3.py` 消息序列化协议
* `protocol_v4.py` `struct` 协议
* `struct_benchmark.py` `struct` 协
