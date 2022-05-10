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

