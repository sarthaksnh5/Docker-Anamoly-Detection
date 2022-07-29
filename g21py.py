from pyod.models.iforest import IForest
from dataSet import trainingData, testData
import matplotlib.pyplot as plt
from joblib import dump, load

clf_name = "IForest"
clf = IForest(n_estimators=2500, contamination=0.0005, behaviour='new')
train_data = trainingData("g21")
clf.fit(train_data)

testDataSet = testData("KV01P0049", "g21")
test_pred = clf.predict(testDataSet)
y_test_scores = clf.decision_function(testDataSet)  # outlier scores

y_data = [i for i in range(len(test_pred))]

fig, ax_left = plt.subplots()
ax_right = ax_left.twinx()

ax_left.plot(test_pred, color="red")
ax_right.plot(testDataSet, color="blue")

plt.show()