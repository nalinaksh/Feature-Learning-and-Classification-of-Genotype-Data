##################################
###CS675, FALL16
###Python script for Naive Bayes
###classifier
###Submitted by: Nalinaksh Gaur
###ucid: ng294
##################################
import sys
import math
import random
#############################
def NB(XTrain, labels, XTest):
    m0 = []
    m1 = []
    col = len(XTrain[0])
    for i in range(col):
        m0.append(1)
        m1.append(1)

    means = {0:m0, 1:m1}
    cnt = [0,0]

    for k in range(len(XTrain)):
        cnt[labels[k]] += 1
        attributes = XTrain[k]
        for i in range(0,len(attributes),1):
            means[labels[k]][i] += float(attributes[i])

    for i in range(col):
        means[0][i] /= cnt[0]
        means[1][i] /= cnt[1]

    var0 = []
    var1 = []

    for i in range(col):
        var0.append(0)
        var1.append(0)

    variances = {0:var0, 1:var1}
    cnt = [0,0]
    for k in range(len(XTrain)):
        cnt[labels[k]] += 1
        attributes = XTrain[k]
        for i in range(0,len(attributes),1):
            variances[labels[k]][i] += math.pow((float(attributes[i])-means[labels[k]][i]),2)

    for i in range(col):
        variances[0][i] /= cnt[0]
        variances[1][i] /= cnt[1]

    predicted = {}
    for t in range(len(XTest)):
        arg0 = 0.0
        arg1 = 0.0
        x = XTest[t]
        for i in range(len(x)):
            arg0 += math.pow( (float(x[i])-means[0][i]),2)/variances[0][i] 
            arg1 += math.pow( (float(x[i])-means[1][i]),2)/variances[1][i] 
        if arg0 < arg1:
            predicted[t] = 0
        else:
            predicted[t] = 1
    
    return predicted
#######################
