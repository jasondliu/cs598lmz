import sys, threading

def run():
    cargarTable()
    root.mainloop()


def onReturn(event):
    print("Cargando usuario")
    user = txtUsuario.get()
    passw = txtPass.get()
    print("user: " + user)
    print("pass: " + passw)
    registrar_usuario(user, passw)
    pass

def getUser():
    return txtUsuario.get()


def cargarTable():
    Label(root, text="Usuario").grid(row=0)
    Label(root, text="Contraseña").grid(row=1)
    txtUsuario = Entry(root, textvariable=user)
    txtPass = Entry(root, show='*')
    txtUsuario.grid(row=0, column=1)
    txtPass.grid(row=1, column=1)
    btLogin = Button(root, text="Login", width=10, command=lambda: registrar_usuario(getUser(), txtPass.
