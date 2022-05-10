import mmap
# Test mmap.mmap read performance

read_payload = [
    '{}{}{}'.format(
        'a' * 100,
        'x' * 1024 * 1024 * 10,
        'b' * 100,
    ) for _ in range(1000)
]


def test_mmap_read(benchmark):
    with open('/tmp/mmap_read.txt', 'w+') as f:
        for p in read_payload:
            f.write(p)

    with open('/tmp/mmap_read.txt', 'r+') as f:
        mm = mmap.mmap(f.fileno(), 0)
        def read():
            for p in read_payload:
                mm.read(len(p))
        benchmark.pedantic(read, rounds=10)


def test_file_read(benchmark):
    with open('/tmp/file_read.txt', 'w+') as f:
        for p in read_payload:
            f.write(p)

