import codecs
codecs.register_error('strict', codecs.ignore_errors)


def create_file():

    config = ConfigParser.ConfigParser()
    config.optionxform = str
    config.readfp(open('config.cfg'))    
    
    #print "Reading config values."
    sen1sensor = config.get('GeoTIFF configurations', 'sen1sensor')
    sen1latname = config.get('GeoTIFF configurations', 'sen1latname')
    sen1lonname = config.get('GeoTIFF configurations', 'sen1lonname')
    sen1timename = config.get('GeoTIFF configurations', 'sen1timename')
    sen1filename = config.get('GeoTIFF configurations', 'sen1filename')
    sen2sensor = config.get('GeoTIFF configurations', 'sen2sensor')
    sen2latname = config.get('GeoTIFF configurations', 'sen2latname')
    sen2lonname = config.get('GeoTIFF configurations', 'sen2lonname')
    sen2timename = config.get('
