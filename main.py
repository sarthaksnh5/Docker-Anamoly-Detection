import schedule
import datetime
import time

from pyod.models.iforest import IForest
from dataSet import trainingData, testData
import matplotlib.pyplot as plt
import pandas as pd
from joblib import dump, load

clf = load('g1.joblib')

def myJob():
    curr_timeStamp = datetime.datetime.now()
    print(f"current time: {curr_timeStamp}")
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



# schedule.every(10).seconds.do(myJob)
# schedule.every(10).minutes.do(job)
schedule.every().hour.do(myJob)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)