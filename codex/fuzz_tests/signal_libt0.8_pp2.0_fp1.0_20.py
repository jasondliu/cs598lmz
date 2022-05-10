import signal
signal.signal(signal.SIGINT, handler)

def poll():
    while(1):

        if d.read_pin(2) == 0:
            print("Alarma Activada")
            led()
            d.write_pin(4, 0)
        else:
            d.write_pin(4, 1)
            alarmaActivada = False
            break


def led():

    d.write_pin(4, 1)
    d.read_pin(2)

    cont = 0
    while cont < 5:

        d.write_pin(4, 1)
        sleep(2)
        d.write_pin(4, 0)
        sleep(2)
        cont += 1
    return


alarmaActivada = True

while(1):


    if d.read_pin(2) == 0:
        if alarmaActivada == True:
            poll()
