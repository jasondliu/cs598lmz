from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(df_final_vars.bdi.tobytes())
#note: loading converted frames will not work due to Byte conversion and compression during export - there
#      may be a way to decompress the numpy arrays but I didn't have time to figure this out and cPickle
#      was slower, so I scrapped it.

if args.preprocess and not os.path.isfile(args.version_directory + '/' + args.ticker_pair + '_processed_data_arrays_' + args.version_name + '_' + str(args.no_of_training_samples) + '_arrays.npz'):
    print('Loading data into memory.')
    data = []
    for i in range(args.no_of_training_samples):
        data.append(BZ2Decompressor().decompress(df_final_vars[df_final_vars['frame_no'] == i][['dt', 'bdi']].values.tobytes()))
    data_arrays_x_y = np.array(
