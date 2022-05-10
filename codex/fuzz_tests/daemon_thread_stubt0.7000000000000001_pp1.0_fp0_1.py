import sys, threading

def run():
    print("Lancement du programme", "*"*10)
    while True:
        pass

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

def stop():
    print("Arrêt du programme")
    sys.exit(0)

signal.signal(signal.SIGINT, stop)

while True:
    pass
</code>
Le problème avec cette solution est que le programme est arrêté sans passer par le destructeur de la classe de la commande.
Pour arrêter la commande avec la méthode <code>stop()</code> de la classe de la commande, il faut appuyer sur ctrl+c deux fois.
<code>import signal, sys, threading

def run():
    print("Lancement du programme", "*"*10)
    while True:
        pass

class Command:
    def __init__(self):
        self.thread = threading.Thread(target=run)

