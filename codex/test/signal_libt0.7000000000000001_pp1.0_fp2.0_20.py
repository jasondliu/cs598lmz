import signal
signal.signal(signal.SIGINT, sigint_handler)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Logger & H5
logger = Logger(fname='TB_log.txt', on_screen=True, overwrite=True)
#h5_fname = 'TB_results.h5'
#h5_fname = 'TB_results_' + str(time.time()) + '.h5'
#h5_fname = 'TB_results_' + str(time.time()) + '.h5'
#res_h5 = h5py.File(h5_fname, 'w')
#res_h5.attrs['date'] = str(datetime.now())
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Input Parameters
input_img_row = 32
input_img_col = 32
input_img_num = 1
input_img_chn = 4
input_img_dpt = 1

output_img_row = 32
output_img_col = 32
