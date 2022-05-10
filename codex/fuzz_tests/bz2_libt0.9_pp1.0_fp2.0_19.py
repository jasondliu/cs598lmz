import bz2
bz2.decompress(packet)

packet = bz2.compress(packet)
packet
shutil.copyfileobj(StringIO.StringIO(packet), fout)
fout.close()

fin = open('compressed_packet.pcap', 'rb')
pcap = dpkt.pcap.Reader(fin)

i = 0;
for ts, bfp in pcap:
	print ts,
	i=i+1
	if(i==1):
	    bz2data = bfp
	    offsetlen = struct.unpack('<H', bz2data[2:4])[0] - 64
	    print offsetlen
	if(i>1):
		bz2data = bfp[offsetlen:]
	print bz2.decompress(bz2data)
