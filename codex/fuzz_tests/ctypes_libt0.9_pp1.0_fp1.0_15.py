import ctypes
ctypes.windll.kernel32.SetConsoleMode(handle, 7)

print("Press ESC to stop")
while True:
    key = msvcrt.getch()
    if key == escape:
        exit()

    if key in alphabet:
        if key in keylist:
            if timeout > 0:
                msvcrt.putwch(" ")
                count = 1

        else:
            timeout = 100
            count += 1
            keylist.append(key)
            msvcrt.putwch(key)
    else:
        if count >= word_len:
            words += 1
            count = 1
            msvcrt.putwch(" ")
            timeout = 100
            keylist.clear()

        else:
            keylist.clear()
            timeout = 100
            count = 1

    if timeout <= 0:
        words += 1
        count = 1
        keylist.clear()
        msvcrt.putwch(" ")

    else:
        timeout -= 1
        sleep(10 / 1000)

    if msvcr
