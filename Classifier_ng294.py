##################################
###CS675, FALL16
###Python script for creating a 
###set of classifiers and feature 
###selection algorithms 
###Submitted by: Nalinaksh Gaur
###ucid: ng294
##################################

import sys
import math
import random
import Fscore as fs
import NaiveBayes
import NearestMeans
import LinearSVC
#############################
##Read traindata and
##store each line indexed by
##its line number in a dictionary
#############################
def parseData(datafile):
    fd = open(datafile, "r")
    data = {}
    rows = 0
    for line in fd:
        row = []
        row = line.split()
        data[rows] = row
        rows += 1

    return data
#############################
##Read training labels and
##resp. indices in data file
#############################
def parseLabels(trainfile):
    ft = open(trainfile,"r")
    labels = {}
    for line in ft:
        t = line.split()
        labels[int(t[1])] = int(t[0])
    return labels
##########################
##Predict labels of test
##using cross validation
##########################
def Classify(XTrain,labels, XTest):

    Pred_NM = NearestMeans.NM(XTrain, labels, XTest)
    Pred_NB = NaiveBayes.NB(XTrain, labels, XTest)
    Pred_SVC = LinearSVC.SVC(XTrain, labels, XTest)
    print("Test labels:")
    for t in range(len(XTest)):
        vote = majorityVote(Pred_NM[t], Pred_NB[t], Pred_SVC[t])
        print(vote,t)
############################
##Compute majority vote
#############################
def majorityVote(p, q, r):
    cnt = [0,0]
    cnt[p] += 1
    cnt[q] += 1
    cnt[r] += 1
    return cnt.index(max(cnt))
#############################    
#Compute number of positive
#and negative instances in 
#the dataset
#############################
def comp_stats(labels):
    count = [0,0]
    d = {}
    inst_pos = []
    inst_neg = []
    for i in labels:
        count[labels[i]] += 1
        if(labels[i] == 0):
            inst_neg.append(i)
        else:
            inst_pos.append(i)
    d[0] = inst_neg
    d[1] = inst_pos
    return [count, d]
#############################
##main function
#############################
def main():
    trainfile = sys.argv[1]
    labelfile = sys.argv[2]
    testfile  = sys.argv[3]
    traindata = parseData(trainfile)
    labels = parseLabels(labelfile)
    testdata = parseData(testfile)
    col = len(traindata[0])
    rows = len(traindata)

    #Compute stats
    res = comp_stats(labels)
    count = res[0]
    instances = res[1]
    pos = count[1]
    neg = count[0]
    inst_neg = instances[0]
    inst_pos = instances[1]

     
    ##Compute F-Score of all features
    scores = []
    for j in range(col):
        f = []
        F_Score = fs.Fscore(traindata, labels, rows, j, pos, inst_pos, neg, inst_neg)
        f = [F_Score, j]
        scores.append(f)
    
    scores = sorted(scores, reverse=True)
    colSubset = []
    for j in range(45):
        colSubset.append(scores[j][1])
    colSubset = sorted(colSubset)
    print("Total number of features: %d" % len(colSubset))
    print("Feature column numbers used for final prediciton: ")
    print(colSubset)

    #New Training Data set after feature selection
    x = []
    XTrain = []
    for i in range(rows):
        x = []
        for j in colSubset:
            x.append(float(traindata[i][j]))
        XTrain.append(x)

    #New Test Data set after feature selection
    xt = []
    XTest = []
    for i in range(len(testdata)):
        xt = []
        for j in colSubset:
            xt.append(float(testdata[i][j]))
        XTest.append(xt)

    #Build classifiers using train data to predict labels of test data
    Classify(XTrain, labels, XTest) 
#############################
if __name__ == "__main__":
    main()
