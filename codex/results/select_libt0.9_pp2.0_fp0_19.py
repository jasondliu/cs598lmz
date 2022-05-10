import select
+
+def server(adres):
+	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+	sock.bind(adres)
+	sock.listen(1)
+	while True:
+		cliente, endereco = sock.accept()
+		print('Cliente conectado:', endereco)
+		cliente.send(b'\n   Bem vindo ao bate-papo!\n')
+		threading.Thread(target = conversa, args =
+			(cliente, endereco)).start()
+
+def conversa(cliente, endereco):
+	clientes[cliente] = endereco
+	try:
+		while True:
+			msg = cliente.recv(4096)
+			if not msg:
+			
