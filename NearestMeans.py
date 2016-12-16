##################################
###CS675, FALL16
###Python script for Nearest Means
###classifier
###Submitted by: Nalinaksh Gaur
###ucid: ng294
##################################
import sys
import math
import random
#############################
def NM(XTrain, labels, XTest):
    m0 = []
    m1 = []
    col = len(XTrain[0])
    for i in range(col):
        m0.append(0)
        m1.append(0)

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

    predicted = {}
    for t in range(len(XTest)):
        arg0 = 0.0
        arg1 = 0.0
        x = XTest[t]
        for i in range(len(x)):
            arg0 += math.pow( (float(x[i])-means[0][i]),2) 
            arg1 += math.pow( (float(x[i])-means[1][i]),2) 
        if arg0 < arg1:
            predicted[t] = 0
        else:
            predicted[t] = 1
    
    return predicted
#######################
