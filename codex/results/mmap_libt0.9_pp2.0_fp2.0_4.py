import mmap
import time
import sys


# in memory of mappers
mapper_data = [0, 0]


def mapper(filename):
    """Mapper spamfunction."""
    print("Mapper process started")
    start = time.time()
    file_size = mapper_data[1]
    mapper_data[0] = True
    with open(filename, 'rb', 0) as file:
        s = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        # s = file.read()

        total = ''.join([s[i:i + 4] for i in range(0, file_size, 4)]).count('spam')
        print("Mapper process completed")
        print("Mappers result: ", total)
        mapper_data[0] = False
        mapper_data[1] = total
        print("Mapper time: ", time.time() - start)


def combiner(filename):
    """Combiner spamfunction."""
    print("Combiner process started")
   
