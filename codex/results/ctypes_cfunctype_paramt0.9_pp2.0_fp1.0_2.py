import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)
class semg_processor_new(object):
    def __init__(self, sel):
        self.predictor = FUNTYPE(None)
        self.test = FUNTYPE(None)
        if sel == 'wo':
            self.mode_label = 'withoung-doublearms-dynamic-joint-40'
            self.predictor = FUNTYPE(semg_processor_new_wo_predictor)
        elif sel == 'wo-doublearms-30':
            self.mode_label = 'without-doublearms-30'
            self.predictor = FUNTYPE(semg_processor_new_wo_doublearms_thirty_predictor)
        elif sel == 'stacked-width-dense':
            self.mode_label = 'withoung-doublearms-dynamic-joint-stacked-width-dense'
            self.predictor = FUNTYPE(semg_processor_new_stacked_wo_width_dense_predictor)
        elif se
