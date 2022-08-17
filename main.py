import requests
from joblib import load
from dataSet import testData
import os
import numpy
import schedule
import datetime
import time
import warnings
from influxdb_client.client.warnings import MissingPivotFunction
warnings.simplefilter("ignore", MissingPivotFunction)


anamoly = [
    {
        "method": "anamoly1",
        "version": "v1",
        "interval": 2,
        "unit": "hours",
        "dataCount": 86400,
        "params": {
            "g1": {
                "url": "http://192.168.1.8/g1.joblib"
            }
        }
    },
]


def mainFunc(anamoly):
    if anamoly['version'] == 'v1':
        model_name = 'g1_model.joblib'
        parameter = list(anamoly['params'].keys())[0]
        print(parameter)
        model_url = anamoly['params'][parameter]['url']

        r = requests.get(model_url)
        open(model_name, 'wb').write(r.content)

        clf = load(model_name, parameter)

        print("[STATUS] Model Done")

        myJob(clf)

        print("[STATUS] Deleting model")
        os.remove(model_name)


def myJob(clf, param):
    curr_timeStamp = datetime.datetime.now()
    print(f"current time: {curr_timeStamp}")
    testDataSet = testData("KV01P0049", param)
    test_pred = clf.predict(testDataSet)

    unique, count = numpy.unique(test_pred, return_counts=True)
    data = dict(zip(unique, count))
    print("Count of anamoly: ", end="")
    print(data[1])

# for item in anamoly:
    # mainFunc(item)
    # if item['unit'] == 'hours':
        # schedule.every(item['interval']).hours.do(myJob)
    # elif item['unit'] == 'seconds':
        # schedule.every(item['interval']).seconds.do(myJob)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


mainFunc(anamoly[0])
