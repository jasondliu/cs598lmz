import select
# Test select.select

servers = [ Server('127.0.0.1', 8001),
            Server('127.0.0.1', 8002),
            Server('127.0.0.1', 8003)]

selectables = []

for server in servers:
    selectables.append(server)

while True:
    print('selecting')
    # select.select requires a timeout
    rs, ws, es = select.select(selectables, [], [])
    if not rs:
        print('No response')
        continue
    for s in rs:
        print(s.process())
</code>
This attempt fails with:
<code>Traceback (most recent call last):
  File "C:\Users\Kubik\Downloads\select-test.py", line 39, in &lt;module&gt;
    rs, ws, es = select.select(selectables, [], [])
  File "C:\Python27\lib\socket.py", line 168, in __getattr__
    raise AttributeError(name)
AttributeError: fil
