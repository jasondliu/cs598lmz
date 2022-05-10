import sys, threading

def run():
	timeline = []
	for line in sys.stdin:
		line = line.strip()
		if line.startswith("***"):
			timeline.append(line)
		else:
			timeline[-1] += line
	return timeline

def main():
	timeline = run()
	for event in timeline:
		print event

if __name__ == "__main__":
	main()
