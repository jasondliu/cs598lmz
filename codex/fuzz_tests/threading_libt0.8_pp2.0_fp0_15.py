import threading
threading.stack_size(512*1024) # 512MB stack
sys.setrecursionlimit(2**20)  # approx 1 million recursions

def initialize_screen(screen, board, size):
    screen.fill((0, 0, 0))
    for i in range(len(board)):
        for j in range(len(board[0])):
            pygame.draw.rect(screen, pygame.Color('white'), (i * size, j * size, size, size))
            if board[i][j] == 1:
                pygame.draw.circle(screen, pygame.Color('black'), (int((i + 0.5) * size), int((j + 0.5) * size)), int(size / 2.0))
    pygame.display.flip()


def start_game(screen, size):
    play_again = True
    while play_again:
        play_again, minutes, seconds = start_timer(screen)

        pygame.draw.rect(screen, pygame.Color('red'), (0, 0, size * len(board),
