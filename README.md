# EEET2574 | Assignment 2: Data Pipeline for Dutch Energy

Name: Pham Xuan Dat 

Student ID: s3927188

# Introduction 

The submission is structured as follows:
```
.
├── databrick-notebooks/
│   └── EEET2574 - Asm2 - s3927188.dbc
├── jupyter-notebooks
│   ├── Dockerfile
│   ├── notebook
│   │   ├── data_raw_gathered
│   │   │   ├── data-electricity.csv
│   │   │   └── data-gas.csv
│   │   ├── EEET2574-Electricity.ipynb
│   │   ├── EEET2574-Gas.ipynb
│   │   └── EEET2574-Main.ipynb
│   ├── requirements.txt
│   ├── Dockerfile
│   └── setup.sh
├── mongo-upload
│   ├── data
│   │   ├── Electricity
│   │   │   ├── coteq_electricity_2018.csv
│   │   │   ├── coteq_electricity_2019.csv
│   │   │   ...
│   │   └── Gas
│   │       ├── coteq_gas_2018.csv
│   │       ├── coteq_gas_2019.csv
│   │       ...
│   ├── Dockerfile
│   ├── mongoUpload.py
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

To ensure stability, most of the work will be run in Docker environment. 

- Module `mongo-upload` contains a script that gathers raw data files `.csv` and upload them to MongoDB. 

- Module `jupyter-notebooks` and `databrick-notebook` contains the following files:

  - `EEET2574-Electricity`, `EEET2574-Gas`: For data processing and model training
  
  - `EEET2574-Main`: For answering the assignment questions

# How to run

## Task 1: MongoDB 

Boot up container `mongo-upload` to start reading `csv` file and uploading to MongoDB

```
$ docker compose -f ./docker-compose.yml up mongo-upload --build
```

The reason why we don't detach this container is we should wait and check until it has done scanning and uploading all the files. 

![alt text](https://i.imgur.com/r8Psa8Z.png)

If successfully, our database atlas will look as follows:

![alt text](https://i.imgur.com/Miby0Nw.png)

Furthermore, since the connection with MongoDB server can be unstable at times, it is recommended to use different database name to prevent intefering with the subsequent modules (i.e. model training) 

```py
# mongoUpload.py
...
db = client.get_database('db-name') #use different db name here 
```

## Task 2-4: Data Ingestion and Cleaning / Transformation

Task 2 and 3 will be presented via two modules `databrick-notebook` and `jupter-notebook`. Whereas both serves data processing, visualization and model training, the latter serves as a fallback in case we cannot import to Databricks platform (like this [thread](https://community.databricks.com/t5/databricks-free-trial-help/community-edition-isnt-t-supporting-importing-dbc-file/td-p/102239) for example). 

It is noted that using `jupyter-notebook` bears some limitations compared to `databrick-notebook` such as usual kernel crash due to high training workload, or lack of intuitive platform for model tracking.  

- For `databrick-notebooks` we just need to import the file `EEET2574-Asm2.dbc` to the platform. 

- For `jupyter-notebook` we first initiate the notebook

```
$ docker compose -f ./docker-compose.yml up jupyter-notebooks --build --detach
```

And access the notebooks at local site [`localhost:8888`](http://localhost:8888)
