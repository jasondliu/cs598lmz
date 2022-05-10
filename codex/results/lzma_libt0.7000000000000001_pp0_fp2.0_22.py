import lzma
lzma.LZMA_OPTIONS

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def load_image(name):
    image = pygame.image.load(name)
    image = image.convert()
    colorkey = image.get_at((0,0))
    image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print ('Cannot load sound:', fullname)
        raise SystemExit(message)
    return sound

def load_music(name):
    pygame.mixer.music.load(name)

class Player(pygame.spr
