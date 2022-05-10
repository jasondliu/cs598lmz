import sys, threading

def run():
    #for i in range(100)():
    while(1):
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':

    t = threading.Thread(target=func)
    t.start()

    main()
