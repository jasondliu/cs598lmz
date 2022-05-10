import select
+
+#Inicializando as variáveis
+server_address = ('localhost', 8080)
+server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
+server_socket.bind(server_address)
+server_socket.listen(5)
+
+# Adicionando o socket do servidor na lista de sockets que devem ser monitorados
+open_client_sockets = []
+messages_to_send = []
+
+def send_waiting_messages(wlist):
+    for message in messages_to_send:
+        (client_socket, data) = message
+        if client_socket in wlist:
+            client_socket.send(data)
+            messages_to_send.remove(message)
+            
+while True:
+    # Monitora as conexões de entrada e de saída
+
