import ctypes
ctypes.windll.user32.SetProcessDPIAware()


# 创建窗口
wnd = pygame.display.set_mode((800, 600), 0, 32)
# 设置窗口标题
pygame.display.set_caption("Hello, World!")

# 加载并转换图像
# 语法：pygame.image.load(path)
# 返回 Surface 对象
ball = pygame.image.load("ball.png").convert_alpha()

# 在窗口上渲染图像
# 语法：Surface.blit(source, dest, area=None, special_flags = 0) -> Rect
# 将图像 source 在 dest 位置绘制
# area 指定绘制区域

