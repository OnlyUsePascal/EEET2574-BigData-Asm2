import os
import time
import pymongo
import pandas as pd
from dotenv import load_dotenv

# load env
load_dotenv()


def get_env(envName, default):
    return os.environ.get(envName) if os.environ.get(envName) else default


MONGO_URL = get_env('MONGO_URL', 'None')
# load csv
print('=== read csv ===')
dataDir = 'data'
csvFiles = [f'{dataDir}/{file}' for file in os.listdir(dataDir)]

# read
csvFile = csvFiles[0]
df = pd.read_csv(csvFile)
# print(df.head(10))

# connect db
print('=== connect db ===')
client = pymongo.MongoClient(MONGO_URL)
db = client.get_database('db_test1')
coll = db['coll_test1']

coll.drop()
coll.insert_many(df.to_dict('records'))