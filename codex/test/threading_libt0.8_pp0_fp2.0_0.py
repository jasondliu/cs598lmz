import threading
threading.stack_size(1024 * 1024 * 500)


# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------

# 画像ロード
def imageLoad(file, x, y):
    image = pygame.image.load(file).convert_alpha()
    imageX = image.get_width()
    imageY = image.get_height()
    rect0 = [(x, y), (imageX, imageY)]
    return [image, imageX, imageY, rect0]

# 画像切り抜き
def imageCrop(image, crop):
    rect0 = [crop[0], (crop[1], crop[2])]
    image.set_clip(rect0)
    rect1 = image.subsurface(image.get_clip())
    rect2 = rect1.convert()
    rect2.set_colorkey(0)
    rect2 = [rect2, crop[1], crop[2]]
    return rect2

# 画像移動
