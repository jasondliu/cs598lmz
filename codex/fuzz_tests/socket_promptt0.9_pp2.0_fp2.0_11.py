import socket
# Test socket.if_indextoname
if_indextoname_stats = Counter()
if_indextoname_stats.update({"if_indextoname_error": 0})
if_indextoname_stats.update({"if_indextoname_success": 0})
if_indextoname_stats.update({"if_indextoname_total_time": 0})
if_indextoname_stats.update({"if_indextoname_total_count": 0})

def if_indextoname_tester_worker():
	try:
		start_time = time.time()
		socket.if_indextoname(1)
		end_time = time.time()
		if_indextoname_stats.update({"if_indextoname_success": 1})
		if_indextoname_stats.update({"if_indextoname_total_time": end_time - start_time})
	except:
		if_indextoname_stats.update({"if_indextoname_error":
