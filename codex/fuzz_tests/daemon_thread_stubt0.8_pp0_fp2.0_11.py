import sys, threading

def run():
    global win, screen_width, screen_height
    win = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Mole Escape')

    run_loop()
    pygame.quit()


# основной цикл программы
def run_loop():
    global FPS, clock

    while 1:
        clock.tick(FPS)
        update()
        draw()


# обновление всех объектов
def update():
    global stage, mouse_pos, click
    if stage == 0:
        main_menu()
    elif stage == 1:
        game()
    elif stage == 2:
        rules()
    elif stage == 3 and click:
        stage = 0

    # обновляем позицию мыши
    mouse_
