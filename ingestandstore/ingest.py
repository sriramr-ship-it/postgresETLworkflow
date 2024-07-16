import psycopg2

def ingest_data():
   conn = psycopg2.connect(database="postgres", user="postgres", password="pass123", host="localhost", port="5432")
   # Create a cursor object to execute SQL queries
   cur = conn.cursor()
   # Execute CREATE TABLE and COPY operations to retrieve data from csv file and ingest to table AB_NYC_6
   cur.execute("CREATE TABLE AB_NYC_6(id         integer,     name       varchar(1024) NOT NULL,    host_id    integer NOT NULL,    hostname   varchar(1024),    neighbourhood_loc   varchar(1024) NOT NULL,    neighbourhood_area  varchar(1024) NOT NULL,    latitude   float NOT NULL,    longitude  float NOT NULL,    room_type  varchar(2048) NOT NULL,    price      integer NOT NULL,    minimum_nights integer NOT NULL,    number_of_reviews integer, last_review DATE,  reviews_per_month float, calculated_host_listings_count INTEGER NOT NULL, availability_365 INTEGER NOT NULL, PRIMARY KEY(id))")
   cur.execute("COPY ab_nyc_6(id, name, host_id, hostname, neighbourhood_loc   ,neighbourhood_area  , latitude   , longitude  , room_type  ,price, minimum_nights, number_of_reviews, last_review,  reviews_per_month, calculated_host_listings_count, availability_365  ) FROM '/tmp/AB_NYC_2019.csv' DELIMITER ','CSV HEADER;")
   conn.commit()
   cur.close()
   conn.close()
          
