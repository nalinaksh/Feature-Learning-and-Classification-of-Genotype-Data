import sys
import math
import random as rand
rand.seed(1)

from sklearn import svm

###############################
###LinearSVC from scikit-learn
###############################
def SVC(XTrain, labels, XTest):
    X = []
    Y = []
    for i in range(len(XTrain)):
        X.append(XTrain[i])
        Y.append(labels[i])
    test_data = []
    for t in range(len(XTest)):
        test_data.append(XTest[t])

    clf = svm.SVC(kernel='linear', C = 1.0)
    clf.fit(X,Y)

    predicted = {}
    plabels = []
    plabels = clf.predict(test_data)
    p = 0
    for t in range(len(XTest)):
        predicted[t] = plabels[p]
        p += 1
    return predicted
#################################
