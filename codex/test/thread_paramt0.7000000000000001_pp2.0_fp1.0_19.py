import sys, threading
threading.Thread(target=lambda: None).start()

sys.path.insert(0, '../build/Release')

import kalman, util

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("usage: python %s <dataset>" % sys.argv[0])
    exit(1)

  dataset = util.load_dataset(sys.argv[1])
  kalman.run(dataset)
