import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

# SVM are well suited for classification of complex but low or medium sized datasets like the breast cancer dataset provided in sklearn.datasets

# Importing dataset form sklearn.datasets
cancer = datasets.load_breast_cancer()

# Making the input variable x and target y
x = cancer.data
y = cancer.target

# Splitting dataset into train and test splits
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(cancer.data,cancer.target,test_size=0.2)


classes = ['malignant','benign']

# Running state vector classifier with 'linear' kernel and C hyperparameter set as 1
clf =svm.SVC(kernel="linear",C=1)

# Fitting to x_train and Y_train
clf.fit(x_train,y_train)

# Prediction
y_pred = clf.predict(x_test)

# Checking accuracy of the algorithm using metrics module of sklearn
acc = metrics.accuracy_score(y_test,y_pred)


print("Accuracy of svm : ",round(100*acc,2))

#for i in range(10):
#    print("Actual : ", classes[y_test[i]],"Prediction: ",classes[y_pred[i]])