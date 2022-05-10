import select
# Test select.select

servers = [ Server('127.0.0.1', 8001),
            Server('127.0.0.1', 8002),
            Server('127.0.0.1', 8003)]

selectables = []
