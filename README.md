This repository postgresETLworkflow describes tasks to do data ingestion and storage, etl process and workflow management with Metaflow.

The directory ingestandstore has files to implement data ingestion by loading Airbnb New York City dataset from Kaggle. The dataset is downloaded to local machine in .csv format. PostgreSQL is setup in local machine and the table abc_nyc6
is created in postgreSQL with appropriate schema to handle the dataset. 

The directory etlprocess has files to implement ETL process of data extraction, transformation and loading. psycopg2 library is used for the implementation. The data is extracted from postgreSQL db/table ab_nyc6 and transformation is done to 
calculate additional metrics such as avg price per neighborhood etc and missing values are flagged with some special symbols. A new table new_table is created and transformed table into the new_table. 

The workflow implementation is done using Metaflow. The files metaflowetl.py and metaflowetlwithretry.py are used for the implementation. The ETL process workflow is implemented in file metaflowetl.py and graceful failure handling using retry mechanism
is implemented using metaflowetlwithretry.py file.

The instructions for running the project are below:

# Repository:
i) create a new repository on the command line
echo "# postgresETLworkflow" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sriramr-ship-it/postgresETLworkflow.git
git push -u origin main

ii) push an existing repository from the command line
git remote add origin https://github.com/sriramr-ship-it/postgresETLworkflow.git
git branch -M main
git push -u origin main

# Ingest and Store:
   Install postgreSQL table on local machine or on cloud.
i) Create database "postgres" using command CREATE DATABASE "postgres";
ii) After cloning the repo on the local machine, cd to ingestandstore directory.
iii) To run ingest functionality, please use the command "python3 ingest.py"
For e.g:
 python3 ingest.py 


On postgreSQL db, we can see the table created and data is ingested from dataset from .csv file.
postgres=# \dt



# ETL Process:
   i) On postgreSQL db, drop the table created from previous step 2) so that ETL process can be run smoothly.
   postgres=# DROP TABLE ab_nyc_6;
   DROP TABLE
   postgres=#

   ii) cd to directory etlprocess and run python files for extract
    python3 extract.py > extractout
    vim extractout

   iii) cd to directory etlprocess and run python files for transform
    python3 transform.py > transformout
    vim transformout

   iv) cd to directory etlprocess and run python files for load
   python3 load.py > loadout
   vim loadout 
   etlprocess$

# Workflow management with Metaflow:
   i) On postgreSQL db, drop the table created from previous step 2) so that ETL process can be run smoothly.
   postgres=# DROP TABLE ab_nyc_6;
   DROP TABLE
   postgres=# DROP TABLE new_table;
   DROP TABLE

   ii) cd.. from etlprocess directory (Move to the previous directory from etlprocess directory)
   Run Metaflow file to execute Metaflow for ETL process from postgreSQL db
   python3 metaflowetl.py run > metaflowout
   vim metaflowout 
    

   iii) Run metaflow with retry file to execute Metaflow for ETL process with retry mechanism
   python3 metaflowetl.py run --with retry > metaflowretryout
   vim metaflowretryout
   








