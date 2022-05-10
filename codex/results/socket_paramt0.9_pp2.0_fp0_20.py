import socket
socket.if_indextoname(7)

try:
    import dns
    import dns.resolver
    def lookUp(host):
        try:
          answer = dns.resolver.query(host, 'A', raise_on_no_answer=False)
          for rdata in answer:
            return(host, str(rdata))
        except:
          return(host, "DNS fail")
except:
    print('dns Python package unavailable')

with open(dipFile) as f:
    ipList = f.readlines()

ipList = [x.strip() for x in ipList]

for ip in ipList:
    try:
        domainName = socket.gethostbyaddr(ip)
    except Exception as e:
        print(ip + " - " + str(e))
    if domainName:
        #print(str(domainName[0]))
        r = lookUp(str(domainName[0]))
        print(str(r[0]) + " - " + str(r[1]))
