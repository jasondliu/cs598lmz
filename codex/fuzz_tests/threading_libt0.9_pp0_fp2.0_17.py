import threading
threading.Thread(target=mosaic_collect, args=(tile_list, )).start()

# with open(dst_path, 'r') as f:
#     src_list = json.load(f)
#     mosaic_collect(src_list)
