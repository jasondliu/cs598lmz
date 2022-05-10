import threading
threading.Thread(target=finalizar, args=("Ivan",)).start()

# Se crea la interfaz
app = tk.Tk()
app.title('Musica Python')

# Tamaño de la interfaz
ancho = 320
alto = 240
posicion_x = (app.winfo_screenwidth() // 2) - (ancho // 2)
posicion_y = (app.winfo_screenheight() // 2) - (alto // 2)
app.geometry("%dx%d+%d+%d" % (ancho, alto, posicion_x, posicion_y))

# Se crean los botones de la interfaz
play_photo = tk.PhotoImage(file="icons/play.png")
play_btn = tk.Button(app, image=play_photo, borderwidth=0, command=Play)
play_btn.pack(side='top', padx=5, pady=5)

pause_photo = tk.PhotoImage(file="icons/pause.png")
