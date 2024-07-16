import psycopg2

def load_data():
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(database="postgres", user="postgres", password="pass123", host="localhost", port="5432")
        # Create a cursor object to execute SQL queries
        cur = conn.cursor()
        cur.execute("CREATE TABLE new_table AS TABLE ab_nyc_6")
        cur.execute("SELECT *FROM new_table")
        rows = cur.fetchall()
        # Iterate over the rows and print the data
        for row in rows:
           print(row)

        # Close the cursor and the connection
        conn.commit()
        cur.close()
        conn.close()
