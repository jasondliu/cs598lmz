import bz2
bz2.BZ2File('/mnt/moehlc/idaf/GOES/GOES16/OR_ABI-L2-CMIPF-M3C01_G16_s20182051042179_e20182051042670_c20182051042761.nc.bz2')

#%%

def get_goes_data(filename):
    import xarray as xr
    
    with bz2.open(filename, 'rb') as f:
        file_content = f.read()
        goes_data = xr.open_dataset(file_content)
        
    return goes_data

#%%

goes_data = get_goes_data('/mnt/moehlc/idaf/GOES/GOES16/OR_ABI-L2-CMIPF-M3C01_G16_s20182051042179_e20182051042670_c20182051042761.nc.bz2')

#%%

def process_goes_data(goes_data):
