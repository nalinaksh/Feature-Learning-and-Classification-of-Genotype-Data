##################################
###CS675, FALL16
###Fscore.py
###Python script for computing 
###F-Score of a feaure
###Submitted by: Nalinaksh Gaur
###ucid: ng294
##################################

import sys
import math
import random as rand
rand.seed(1)

############################
#Function to compute F-Score
#of a given feature
############################

def Fscore(data, labels, rows, colno, npos, inst_pos, nneg, inst_neg):
    pmean = 0.0
    nmean = 0.0
    mean = 0.0
    for i in range(rows):
        if(labels[i] == 0):
            nmean += float(data[i][colno])
        else:
            pmean += float(data[i][colno])

    mean = (pmean + nmean)/rows
    pmean = pmean/npos
    nmean = nmean/nneg

    numerator = math.pow((pmean - mean),2) + math.pow((nmean - mean), 2)

    pterm  = 0.0
    nterm  = 0.0

    for i in inst_pos:
        pterm += math.pow((float(data[i][colno]) - pmean),2)
    
    for i in inst_neg:
        nterm += math.pow((float(data[i][colno]) - nmean),2)

    pterm = pterm/(npos -1)
    nterm = nterm/(nneg - 1)

    F_Score = numerator/(pterm + nterm)
    return F_Score
###############################
#scores = []
#for j in range(col):
#    f = []
#    F_Score = Fscore(j)
#    f = [F_Score, j]
#    scores.append(f)

#scores = sorted(scores, reverse=True)

#for i in range(30):
#    print(scores[i])

