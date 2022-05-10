import bz2
bz2_path = pathlib.Path(bz2.__file__)
bz2_path

bz2_path.read_bytes()
bz2_path.read_text()

bz2_path.read_bytes().decode()

bz2_path.read_bytes().decode('utf-8')

bz2_path.stat()

bz2_path.stat().st_mode


bz2_path.stat().st_size

bz2_path.stat().st_size / 1024
bz2_path.stat().st_size / 1024 / 1024

bz2_path.stat().st_size / 1024 / 1024 / 1024

bz2_path.stat().st_size / (1024 ** 3)
