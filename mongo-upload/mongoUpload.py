import os
import time
import pymongo
import pandas as pd
from dotenv import load_dotenv

# load env
print('> Loading env ...')
load_dotenv()
def get_env(envName, default):
    return os.environ.get(envName) if os.environ.get(envName) else default
MONGO_URL = get_env('MONGO_URL', 'None')

# load csv
print('> Getting Data...')
dataDir = 'data'
energyTypes = ['Electricity', 'Gas']

# init db
client = pymongo.MongoClient(MONGO_URL)
db = client.get_database('asm2-test1')
# coll = db['']

for energyType in energyTypes:
    print(f'>> {energyType}')
    # scan files
    dataSubdir = f'{dataDir}/{energyType}'
    csvFiles = [f'{dataSubdir}/{file}' for file in os.listdir(dataSubdir)]
    energyDf = pd.DataFrame()
    
    coll = db[energyType.lower()]
    coll.drop()

    print('- Loading csv')
    for csvFile in csvFiles:
        metadata = csvFile.split('/')[-1].split('.')[0].split('_')
        
        # extract company, year
        company = metadata[0]
        year = metadata[-1]
        
        # read csv + add collumn 
        df = pd.read_csv(csvFile)
        df['company'] = company
        df['year'] = year
        
        # gathering
        energyDf = pd.concat([energyDf, df])
    
        # 
        print(f'- Uploading {csvFile}')
        coll.insert_many(df.to_dict('records'))
    
print('> Done!')