import socket
socket.if_indextoname(1)```

#### arp

* ARP cache에 특정 IP 해당 MAC addr 출력
```ping www.naver.com``` (namerserver IP)
```arp -a HOST_IP```

#### iptables NAT

* 인터넷 가능여부 확인
```ping 8.8.8.8```

* iptables 명령어 기본 사용법
숫자가 아닌 문자열만 명령모드에서 입력하면 된다.
--table 본체는 nat table 대상 
--append 뒤에 따라오는 
