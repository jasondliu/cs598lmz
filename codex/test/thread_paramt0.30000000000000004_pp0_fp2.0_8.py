import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

def get_tiles(img):
    tiles = []
    for i in range(0, img.shape[0], 8):
        for j in range(0, img.shape[1], 8):
            tiles.append(img[i:i+8, j:j+8])
    return tiles

def get_dct(tiles):
    dct = []
    for tile in tiles:
        dct.append(cv2.dct(tile))
    return dct

def get_idct(dct):
    idct = []
    for tile in dct:
        idct.append(cv2.idct(tile))
    return idct

def get_img(idct):
    img = np.zeros((idct[0].shape[0] * 8, idct[0].shape[1] * 8, 3), dtype=np.uint8)
