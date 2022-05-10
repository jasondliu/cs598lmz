import ctypes
ctypes.windll.user32.SetProcessDPIAware()
config = get_config()
if config.wide_format:
    screen_width, screen_height = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
    config.screen_width, config.screen_height = screen_width, screen_height
print('screen size: ', config.screen_width, config.screen_height)
pg.init()
screen = pg.display.set_mode((config.screen_width, config.screen_height))
clock = pg.time.Clock()

font_name = pg.font.match_font(config.font_name)


def draw_text(surf, text, size, x, y):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, config.WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text
