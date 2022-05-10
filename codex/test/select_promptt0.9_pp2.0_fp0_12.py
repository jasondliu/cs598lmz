import select
# Test select.select API
select.select([], [], [], -1)

select.select([], [], [], 0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 0))
s.listen(socket.SOMAXCONN)
os.write(s.fileno(), b'X')
for (r, w, e) in [select.select([s], [], [], 0), select.select([s], [], [])]:
    if (r, w, e) != ([s], [], []):
        print(r, w, e)
        raise SystemExit
select.select([s], [], [])
os.write(s.fileno(), b'X')
try:
    select.select([], [], [s], 0)
except Exception as e:
    print("Exception:", e)

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(s.getsockname())

