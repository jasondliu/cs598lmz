import threading
threading.Thread(target=train).start()

#重置游戏模式
def reset_game(event):
    global game_mode
    system('cls')
    game_mode = 0
    print('[*]游戏模式已重置')

#重置游戏次数
def reset_times(event):
    global times
    system('cls')
    times = 0
    print('[*]游戏次数已重置')

#重置游戏进度
def reset_progress(event):
    global progress
    system('cls')
    progress = 0
    print('[*]游戏进度已重置')

#重置游戏状态
def reset_game_status(event):
    global game_status
    system('cls')
   
