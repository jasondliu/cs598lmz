import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# create a dictionary of parameters
#parameters = {'max_depth':[10,20],'n_estimators':[20,40,60]}
parameters = {'max_depth':[10,20],'n_estimators':[40,60],'learning_rate':[0.01,0.1]}
# create a gridsearch of the parameters
clf = GridSearchCV(ensemble.GradientBoostingClassifier(), parameters, n_jobs = -1)
# fit the gridsearch to the data
clf.fit(train_features, train_labels)
# print the best parameters
print (clf.best_params_)

# extract the best estimator
best = clf.best_estimator_

# fit the best estimator to the data
best.fit(train_features, train_labels)

# use the model to predict the test data
predictions = best.predict(test_features)

#
