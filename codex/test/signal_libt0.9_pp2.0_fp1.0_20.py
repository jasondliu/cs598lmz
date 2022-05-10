import signal
signal.signal(signal.SIGINT, quit_and_save)
signal.signal(signal.SIGTERM, quit_and_save)

# -------------------------------------------------------------------------
# Main loop
# -------------------------------------------------------------------------

while True:
    b = bin(GPIO.input(PIN))
    output()
    if DEBUG:
        print('PORTA:')
        print(b)
        print('.....')

    # opción para activar la conexión WIFI
    if int(b,2) == WIFI_START_CODE:
        wifi_connect()

    # opción para activar el display
    if int(b,2) == DISP_START_CODE:
        with servo_lock:
            display_connect()

    # opción para limpiar la memoria RAM y salir
    if int(b,2) == CLEAN_MEM_CODE:
        print("Limpiando memoria... ")
