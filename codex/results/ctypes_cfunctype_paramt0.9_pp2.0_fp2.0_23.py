import ctypes
FUNTYPE = ctypes.CFUNCTYPE(PGresultP, POINTER(PGconn), STRING)

ret = rlib.PQexec(conn, "select * from pg_user")
for i in range(rlib.PQntuples(ret)):
	print "user ", rlib.PQgetvalue(ret, i, 0)
rlib.PQclear(ret)

rlib.PQfinish(conn)

# vim: ts=4:sts=4:sw=4:noet
