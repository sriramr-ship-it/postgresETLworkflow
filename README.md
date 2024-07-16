This repository postgresETLworkflow describes tasks to do data ingestion and storage, etl process and workflow management with Metaflow.

The directory ingestandstore has files to implement data ingestion by loading Airbnb New York City dataset from Kaggle. The dataset is downloaded to local machine in .csv format. PostgreSQL is setup in local machine and the table abc_nyc6
is created in postgreSQL with appropriate schema to handle the dataset. 

The directory etlprocess has files to implement ETL process of data extraction, transformation and loading. psycopg2 library is used for the implementation. The data is extracted from postgreSQL db/table ab_nyc6 and transformation is done to 
calculate additional metrics such as avg price per neighborhood etc and missing values are flagged with some special symbols. A new table new_table is created and transformed table into the new_table. 

The workflow implementation is done using Metaflow. The files metaflowetl.py and metaflowetlwithretry.py are used for the implementation. The ETL process workflow is implemented in file metaflowetl.py and graceful failure handling using retry mechanism
is implemented using metaflowetlwithretry.py file.

The instructions for running the project are below:

1. Repository:
# create a new repository on the command line
echo "# postgresETLworkflow" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sriramr-ship-it/postgresETLworkflow.git
git push -u origin main

# push an existing repository from the command line
git remote add origin https://github.com/sriramr-ship-it/postgresETLworkflow.git
git branch -M main
git push -u origin main

2. Ingest and Store:
   Install postgreSQL table on local machine or on cloud.
i) Create database "postgres" using command CREATE DATABASE "postgres";
ii) After cloning the repo on the local machine, cd to ingestandstore directory.
iii) To run ingest functionality, please use the command "python3 ingest.py"
For e.g:
~/ingestandstore$ python3 ingest.py 
:~/ingestandstore$

On postgreSQL db, we can see the table created and data is ingested from dataset from .csv file.
postgres=# \dt
          List of relations
 Schema |   Name   | Type  |  Owner   
--------+----------+-------+----------
 public | ab_nyc_6 | table | postgres
(1 row)

postgres=# SELECT *FROM ab_nyc_6;
postgres=# 
 id    |                                                                                        name                                                                                         |  host_id  |              hostname               | neighbourhood_loc |     neighbourhood_area     | latitude | longitude |    room_type    | price | minimum_nights | number_of_reviews | last_review | reviews_per_month | calculated_host_listings_count | availability_365 
----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+-------------------------------------+-------------------+----------------------------+----------+-----------+-----------------+-------+----------------+-------------------+-------------+-------------------+--------------------------------+------------------
     2539 | Clean & quiet apt home by the park                                                                                                                                                  |      2787 | John                                | Brooklyn          | Kensington                 | 40.64749 | -73.97237 | Private room    |   149 |              1 |                 9 | 2018-10-19  |              0.21 |                              6 |              365
     2595 | Skylit Midtown Castle                                                                                                                                                               |      2845 | Jennifer                            | Manhattan         | Midtown                    | 40.75362 | -73.98377 | Entire home/apt |   225 |              1 |                45 | 2019-05-21  |              0.38 |                              2 |              355
     3647 | THE VILLAGE OF HARLEM....NEW YORK !                                                                                                                                                 |      4632 | Elisabeth                           | Manhattan         | Harlem                     | 40.80902 |  -73.9419 | Private room    |   150 |              3 |                 0 |             |                   |                              1 |              365
     3831 | Cozy Entire Floor of Brownstone                                                                                                                                                     |      4869 | LisaRoxanne                         | Brooklyn          | Clinton Hill               | 40.68514 | -73.95976 | Entire home/apt |    89 |              1 |               270 | 2019-07-05  |              4.64 |                              1 |              194
     5022 | Entire Apt: Spacious Studio/Loft by central park                                                                                                                                    |      7192 | Laura                               | Manhattan         | East Harlem                | 40.79851 | -73.94399 | Entire home/apt |    80 |             10 |                 9 | 2018-11-19  |               0.1 |                              1 |                0
     5099 | Large Cozy 1 BR Apartment In Midtown East                                                                                                                                           |      7322 | Chris                               | Manhattan         | Murray Hill                | 40.74767 |   -73.975 | Entire home/apt |   200 |              3 |                74 | 2019-06-22  |              0.59 |                              1 |              129
     5121 | BlissArtsSpace!                                                                                                                                                                     |      7356 | Garon                               | Brooklyn          | Bedford-Stuyvesant         | 40.68688 | -73.95596 | Private room    |    60 |             45 |                49 | 2017-10-05  |               0.4 |                              1 |                0
     5178 | Large Furnished Room Near B'way                                                                                                                                                     |      8967 | Shunichi                            | Manhattan         | Hell's Kitchen             | 40.76489 | -73.98493 | Private room    |    79 |              2 |               430 | 2019-06-24  |              3.47 |                              1 |              220
......
etc
.....

3. ETL Process:
   i) On postgreSQL db, drop the table created from previous step 2) so that ETL process can be run smoothly.
   postgres=# DROP TABLE ab_nyc_6;
   DROP TABLE
   postgres=#

   ii) cd to directory etlprocess and run python files for extract
   HP-Laptop-15s-fq3xxx:~/etlprocess$ python3 extract.py > extractout
   HP-Laptop-15s-fq3xxx:~/etlprocess$ vim extractout

   iii) cd to directory etlprocess and run python files for transform
   admin123@admin123-HP-Laptop-15s-fq3xxx:~/etlprocess$ python3 transform.py > transformout
   admin123@admin123-HP-Laptop-15s-fq3xxx:~/etlprocess$ vim transformout

   iv) cd to directory etlprocess and run python files for load
   admin123@admin123-HP-Laptop-15s-fq3xxx:~/etlprocess$ python3 load.py > loadout
   admin123@admin123-HP-Laptop-15s-fq3xxx:~/etlprocess$ vim loadout 
   admin123@admin123-HP-Laptop-15s-fq3xxx:~/etlprocess$

4. Workflow management with Metaflow:
   i) On postgreSQL db, drop the table created from previous step 2) so that ETL process can be run smoothly.
   postgres=# DROP TABLE ab_nyc_6;
   DROP TABLE
   postgres=# DROP TABLE new_table;
   DROP TABLE

   ii) cd.. from etlprocess directory (Move to the previous directory from etlprocess directory)
   Run Metaflow file to execute Metaflow for ETL process from postgreSQL db
   admin123@admin123-HP-Laptop-15s-fq3xxx:~$ python3 metaflowetl.py run > metaflowout
   Metaflow 2.12.7 executing LinearFlow for user:admin123
   Validating your flow...
    The graph looks good!
    Running pylint...
    Pylint not found, so extra checks are disabled.
    admin123@admin123-HP-Laptop-15s-fq3xxx:~$ vim metaflowout 
    admin123@admin123-HP-Laptop-15s-fq3xxx:~$

   iii) Run metaflow with retry file to execute Metaflow for 
   








