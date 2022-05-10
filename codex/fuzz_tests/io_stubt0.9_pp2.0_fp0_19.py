import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

"""for i in range(100):
    flasq3.run(view)
    for i in range(2):
        if view[i] & 0x80:
            sys.stdout.write("-")
        else:
            sys.stdout.write("+")
        sys.stdout.write("{:+}\n".format(view[i] & 0x7f))
    sys.stdout.flush()"""

lda.lda.lda_change_state(lda.lda.lda_state_type.lda_state_select)

t = threading.Thread(target=flasq3.run, args=(view,))
t.start()

try:
    while not lda.lda.lda_wait_flag:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise KeyboardInterrupt
except KeyboardInterrupt:
    print("Interrupted")

lda.lda.lda_wait_flag = True

t.join()
flas
