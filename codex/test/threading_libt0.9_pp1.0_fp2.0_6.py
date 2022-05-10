import threading
threading.stack_size(2**27)

#Threading for the motion detection in a new thread
try:
    th1 = threading.Thread(target=deteccionMovimiento)
    th1.daemon = True
    th1.start()
except:
    print("Fallo arranque HILO")
    print("Error: unable to start thread")

while(1):
    if fin.isSet(): #Condition control, to exit
        print("FIN DETECCIÓN")
        break;
    envio.wait()
    ret, frame = cap.read()
    envio.clear()
    envio2.set()

    video.write(frame)

    #show
    cv2.imshow('Desideo',frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
video.release()
cv2.destroyAllWindows()
