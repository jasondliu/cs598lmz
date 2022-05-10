import sys, threading

def run():
    print("haha")

# run()
# threading.Timer(1, run).start()

# def s():
#     print("hh")
#     threading.Timer(3,s).start()
# s()



def new_game():
    screen.blit(background, (0, 0))
    #更新屏幕
    pygame.display.flip()

#添加背景音乐
# pygame.mixer.music.load("03.wav")
# pygame.mixer.music.play()

#初始化游戏并创建一个屏幕对象
pygame.init()
background = pygame.image.load("bg.jpg")
pygame.display.set_caption("haha")
screen = pygame.display.set_mode((480,700),0,32)
#创建一艘我的飞机
me =
