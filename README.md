# Feature-Learning-and-Classification-of-Genotype-Data

Developed methods for feature learning and classification of genotype data in Python. Train data consist of 8000 instances of simulated (SNP) genotype data containing 29623 SNPs (total features). 15 SNPs are causal one while remainder are noise.

F-Score is used to select 45 most discriminating features. A set of classifiers including Nearest Means, Naive Bayes and Scikit-learn's SVC are used to train on the data obtained after feature selection. Majority voting is used to predict the labels for test data consisting of 2000 instances. An accuracy of 64.3% is achieved.

Feature selection criterion: 
- F-Score (Fscore.py)

Classification Criterion: Majority Voting
Classifiers used:
- Nearest Means (NearestMeans.py)
- Naive Bayes (NaiveBayes.py)
- Linear SVC from svm (LinearSVC.py)

Python command to run the program:

    python Classifier_ng294.py traindata trueclass.txt testdata
