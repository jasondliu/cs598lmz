import sys, threading

def run():
	global n,d,a,b,c,h,p
	f=open(sys.argv[1]).readlines()
	x=f[0].strip().split()
	n=int(x[0])
	d=int(x[1])
	a=int(x[2])
	b=int(x[3])
	c=int(x[4])
	h=int(x[5])
	p=int(x[6])
	res=0
	for i in range(0,n):
		x=f[i + 1].strip().split()
		hi=int(x[0])
		pi=int(x[1])
		if (h-hi)*a + pi <= p*b:
			res = res + 1
	print >> sys.stderr, res
	fout=open(sys.argv[2], 'w')
	fout.write(str(res))
	fout.write('\n')
	fout.close()
def main():
	global
