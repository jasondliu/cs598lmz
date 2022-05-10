import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\r' + ' ' * (len(sys.stdout.last_value) + 1) + '\r')).start()

#%%
# create and save a random model
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = make_classification(n_samples=10000, n_features=4,
                           n_informative=2, n_redundant=0,
                           random_state=0, shuffle=False)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5,
                                                    random_state=0)
clf = RandomForestClassifier(n_estimators=100, max_depth=2,
                             random_state=0)
clf.fit(X_train, y_train)

#%%
# save the model
