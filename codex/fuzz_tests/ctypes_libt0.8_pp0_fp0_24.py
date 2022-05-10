import ctypes
ctypes.c_wchar_p = ctypes.c_wchar_p

def read_csv(date,i):
    file = '/Users/kazuki/Documents/GitHub/DataScienceBowl2019/data/csv/{}/{}_dicom_info.csv'.format(date,i)
    df = pd.read_csv(file)
    
    return df

def gene_dicom_t(df_t, size, n=0, d=0, z=0, t=0, series=0):
    df_t = df_t.values
    dicom_t = np.zeros((size,size,3),dtype='uint8')
    
    for i in range(df_t.shape[0]):
        file = df_t[i][0]
        x = df_t[i][1]
        y = df_t[i][2] + 512

        ds = dicom.dcmread(file)
        dicom_d = np.asarray(ds.pixel_array
