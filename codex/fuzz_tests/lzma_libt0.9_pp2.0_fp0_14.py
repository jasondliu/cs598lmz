import lzma
lzma.decompress(sentinel.encode('latin-1')).decode('latin-1')

ds1_breeds_lens_func = lambda ds: len(ds.breeds)
ds1_colors_lens_func = lambda ds: len(ds.colors)
ds1_photos_lens_func = lambda ds: len(ds.photos)

ds2_breeds_lens_func = lambda ds: len(ds.breed)
ds2_colors_lens_func = lambda ds: len(ds.color)
ds2_photos_lens_func = lambda ds: len(ds.photo)

manifest = [('Breed', (ds1_breeds_lens_func, ds2_breeds_lens_func), (1, 6)),
            ('Color', (ds1_colors_lens_func, ds2_colors_lens_func), (1, 6)),
            ('Photo', (ds1_photos_lens_func, ds2_photos
