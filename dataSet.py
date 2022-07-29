import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd

INFLUXDB_TOKEN = "gVu_-akkny-IfPa5C0vO9Wk0YPlaY_kLANFSmcQY8QHxA--khUXxa4ByRwiv44JZ1wU8Wna2kKlcqLRTwD8svw=="

token = INFLUXDB_TOKEN
org = "sohil@oizom.com"
url = "https://eu-central-1-1.aws.cloud2.influxdata.com"

print("[INFO] Geting infux Client")
client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

def trainingData(field):
    print("[INFO] Influx Query")
    query = f"""from(bucket: "oizom")
    |> range(start: -10d)
    |> filter(fn: (r) => r["_measurement"] == "POLLUDRON_PRO")
    |> filter(fn: (r) => r["_field"] == "{field}")
    |> filter(fn: (r) => r["deviceId"] == "KV01P0043")
    |> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
    |> drop(columns: ["_start", "result", "_stop", "table", "_field", "_measurement", "deviceId"])
    |> yield(name: "mean")"""

    print("[INFO] Executing Query")
    tables = client.query_api().query_data_frame(query, org="sohil@oizom.com")
    
    tables = tables.to_numpy()
    
    tables = tables[:,[3,2]]
    i = 0
    for index, value in enumerate(tables):
        # tables[index][1] = value[1].strftime("%m/%d/%Y, %H:%M:%S")
        tables[index][1] = i
        i += 1
        
    return tables

def testData(id, field):
    print("[INFO] test Data")
    query = f"""from(bucket: "oizom")
    |> range(start: -1d)
    |> filter(fn: (r) => r["_measurement"] == "POLLUDRON_PRO")
    |> filter(fn: (r) => r["_field"] == "{field}")
    |> filter(fn: (r) => r["deviceId"] == "{id}")
    |> aggregateWindow(every: 5m, fn: mean, createEmpty: false)
    |> drop(columns: ["_start", "result", "_stop", "table", "_field", "_measurement", "deviceId"])
    |> yield(name: "mean")"""
    

    tables = client.query_api().query_data_frame(query, org="sohil@oizom.com")
    tables = tables.to_numpy()
    
    tables = tables[:,[3,2]]
    i = 0
    for index, value in enumerate(tables):
        # tables[index][1] = value[1].strftime("%m/%d/%Y, %H:%M:%S")
        tables[index][1] = i
        i += 1
        
    return tables                                       

