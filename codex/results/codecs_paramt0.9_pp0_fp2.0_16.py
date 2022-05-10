import codecs
codecs.register_error('strict', codecs.ignore_errors)

########################################################################
#
# Flexibility for the parameters for SVM
#
########################################################################
def get_params():
    params = dict(
        C= 0.3,
        kernel_type= RBF,
        degree = 2,
        gamma = 0.2,
        coef0 = 0,
        nu = 0.5,
        eps= 0.001,
        p= 0.1,
        shrinking= 1,
        probability= 0,
        cache_size= 100
    )
    return params

########################################################################
#
# Preprocessing data for SVM
#
########################################################################
def preprocess():
    dataset = getDataSet(cfg.FEATURES_DATA_PATH)
    normalized_features,norm = normalize(dataset)
    testing, training = split_dataset(normalized_features)
    training_label = get_label(training[:])
    testing_label = get_label(testing[:])
    training_instances = get_instances(training[:])

