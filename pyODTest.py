from pyod.models.iforest import IForest
from pyod.models.abod import ABOD
from dataSet import trainingData, testData
import matplotlib.pyplot as plt
import pandas as pd
from joblib import dump, load

# clf_name = "IForest"
# clf = IForest(n_estimators=2500, contamination=0.0005, behaviour='new')
# train_data = trainingData()
# clf.fit(train_data)

# # get the prediction labels and outlier scores of the training data
# y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
# y_train_scores = clf.decision_scores_  # raw outlier scores

# #save the model
# dump(clf, 'clf.joblib')

#load the model
clf = load('g1.joblib')

#predict dataset
testDataSet = testData("KV01P0049", "g1")
test_pred = clf.predict(testDataSet)
y_test_scores = clf.decision_function(testDataSet)  # outlier scores

y_data = [i for i in range(len(test_pred))]

fig, ax_left = plt.subplots()
ax_right = ax_left.twinx()

ax_left.plot(test_pred, color="red")
ax_right.plot(testDataSet, color="blue")
# ax_left.plot(y_train_pred, color="red")
# ax_right.plot(train_data, color="blue")

plt.show()

# visualize(clf_name, train_data, train_data, testDataSet, testDataSet, y_train_pred, test_pred, show_figure=True, save_figure=True)

# contamination = 0.1  # percentage of outliers
# n_train = 200  # number of training points
# n_test = 100  # number of testing points

# X_train, y_train, X_test, y_test = generate_data(
#     n_train=n_train, n_test=n_test, contamination=contamination)

# clf_name = 'KNN'
# clf = ABOD()
# clf.fit(X_train)

# # get the prediction labels and outlier scores of the training data
# y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
# y_train_scores = clf.decision_scores_  # raw outlier scores

# # get the prediction on the test data
# y_test_pred = clf.predict(X_test)  # outlier labels (0 or 1)
# y_test_scores = clf.decision_function(X_test)  # outlier scores

# # it is possible to get the prediction confidence as well
# y_test_pred, y_test_pred_confidence = clf.predict(X_test, return_confidence=True)  # outlier labels (0 or 1) and confidence in the range of [0,1]
# fig, ax_left = plt.subplots()
# ax_right = ax_left.twinx()

# ax_left.plot(y_test_pred, color="red")
# ax_right.plot(y_test, color="blue")
# plt.show()

# # visualize(clf_name, X_train, y_train, X_test, y_test, y_train_pred,
# #           y_test_pred, show_figure=True, save_figure=False)