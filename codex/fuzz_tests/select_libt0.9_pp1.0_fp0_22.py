import select_region

def eval_raster_area(raster_path, progress_callback):
    progress_callback.emit(0)
    raster = gdal.Open(raster_path)
    bands_num = raster.RasterCount
    px = raster.GetGeoTransform()[1]
    py = -raster.GetGeoTransform()[5]
    xs = int((raster.RasterXSize)*px)
    ys = int((raster.RasterYSize)*py)
    arr_area = np.array([xy[0]*xy[1] for xy in [(xs, ys)]])
    #import pdb; pdb.set_trace()
    for bi in range(bands_num):
        arr_area += np.array([xy[0]*xy[1] for xy in raster.GetRasterBand(bi+1).GetStatistics(0,1)])
    raster = None
    progress_callback.emit(50)
    return float(format(arr_area.sum(), '.
