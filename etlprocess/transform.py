import psycopg2

def transform_data():
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(database="postgres", user="postgres", password="pass123", host="localhost", port="5432")
        # Create a cursor object to execute SQL queries
        cur = conn.cursor()
        # Execute a SELECT query to retrieve data
        cur.execute("SELECT *  FROM ab_nyc_6")
        # Fetch average price of neighborhood
        cur.execute("SELECT AVG(price) AS transformed_column FROM ab_nyc_6 GROUP_BY(neighbourhood_loc)")
        rows = cur.fetchall()
        # Iterate over the rows and print the data
        for row in rows:
           avg = row

        #conn = psycopg2.connect(database="pgres", user="postgres", password="pass123", host="localhost", port="5432")

        #cur2 = conn.cursor()
        #cur2.execute("INSERT INTO targettbl (avg_price) VALUES(%s)", (avg))

        #print(str(avg))

        #Replace missing date values with special flag -infinity
        cur.execute("SELECT COALESCE(last_review, '-infinity') AS last_review FROM ab_nyc_6")

        rows = cur.fetchall()
        # Iterate over the rows and print the data
        for row in rows:
           print(row)

        #Replace missing reviews_per_month values with special value 0
        cur.execute("SELECT COALESCE(reviews_per_month, 0) AS reviews_per_month FROM ab_nyc_6")

        rows = cur.fetchall()
        # Iterate over the rows and print the data
        for row in rows:
           print(row)

        # Replace missing hostname values with empty string ""
        cur.execute("SELECT COALESCE(hostname, '') AS hostname FROM ab_nyc_6")

        rows = cur.fetchall()
        #Iterate over the rows and print the data
        for row in rows:
           print(row)
