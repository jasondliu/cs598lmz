import threading
threading.Thread(target=draw).start()

pygame.display.update()
clock = pygame.time.Clock()

close = False

while not close:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                close = True

    while len(p.distances) &gt; 300:
        p.distances.pop(0)

    clock.tick(15)
pygame.quit()
</code>


A:

<code>draw</code> and <code>p.update</code> have to use global variables which have to be accessed by all threads. These are the lists/deques <code>p.distances</code> and <code>p.time</code> and <code>close</code>.
Since you have only 2 states, you have to to lock the access to these variables when the thread is not in the state "read the value".
Give the threads exclusive
