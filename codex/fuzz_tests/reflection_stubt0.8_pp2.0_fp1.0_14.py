fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# assert numpy.all(features == features_ref)
# print('numpy.all(features == features_ref)', numpy.all(features == features_ref))
#
# features = features_impl(img, haar_like_feature_coord)
# assert numpy.all(features == features_ref)
# print('numpy.all(features == features_ref)', numpy.all(features == features_ref))
#
# features = features_impl(img, haar_like_feature_coord)
# assert numpy.all(features == features_ref)
# print('numpy.all(features == features_ref)', numpy.all(features == features_ref))
