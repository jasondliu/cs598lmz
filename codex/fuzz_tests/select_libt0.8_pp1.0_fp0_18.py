import select_feature
from sklearn import cross_validation
from sklearn.datasets import load_iris
from sklearn.svm import SVC
f = open('E:/Mashasha/project/xml_coba/training.txt')
doc = [] #list of documents
#labels = [] #list of labels
#for line in f:
#    values = line.split()
#    doc.append(values[0])
#    labels.append(values[1])
for line in f:
	doc.append(line)

#print doc
#print labels

#print len(doc)
#print len(labels)
extract_feature = select_feature.extract_feature
labels = [0,1,2]
extract_feature(doc,labels)
X, y = load_iris(return_X_y=True)
clf = SVC(kernel='linear')
scores = cross_validation.cross_val_score(clf, X, y, cv=5)
#print(scores)
score = scores.mean()
