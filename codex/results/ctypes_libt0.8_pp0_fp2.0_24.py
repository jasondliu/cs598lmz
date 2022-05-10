import ctypes
ctypes.CDLL('/usr/local/lib/libboost_python.dylib').boost_python_module_init()
</code>
Step 3:  install everything to the correct python installation
<code>cd ~

/anaconda/bin/pip install --upgrade --no-cache-dir pip

/anaconda/bin/pip install --upgrade --no-cache-dir setuptools

/anaconda/bin/pip install --upgrade --no-cache-dir wheel

/anaconda/bin/brew install --build-from-source boost

/anaconda/bin/brew install --build-from-source scipy

/anaconda/bin/brew install --build-from-source gdal

/anaconda/bin/brew install --build-from-source pyproj

/anaconda/bin/brew install --build-from-source rasterio

/anaconda/bin/pip install --no-cache-dir geopandas

/anaconda/bin/pip install --no-cache-dir cartopy


