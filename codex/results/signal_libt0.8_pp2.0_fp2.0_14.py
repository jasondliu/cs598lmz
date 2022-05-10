import signal
signal.signal(signal.SIGINT, lambda x,y: sys.exit(0))

def main():
	p = ParticleSimulator(0.001)
	p.init(N)
	p.solve()
	# p.solve(TMAX, DT)

if __name__ == '__main__':
	main()
