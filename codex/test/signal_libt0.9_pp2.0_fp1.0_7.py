import signal
signal.signal(signal.SIGINT, handler)

# obtenemos el puerto de entrada del stacker
port = int(os.environ['PORT'])

if __name__ == '__main__':


	# lanza el juego
	game = Game("Snack", 480, 640)
	pygame.display.set_caption("Snack")

	player = Player("Mario")
	socketio.emit("data",player.to_json(), namespace='/test')
	game.start()
	# emitimos los socket de registrarse y loguearse

