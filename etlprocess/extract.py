import psycopg2

def extract_data():
   # Connect to the PostgreSQL database
   conn = psycopg2.connect(database="postgres", user="postgres", password="pass123", host="localhost", port="5432")
   # Create a cursor object to execute SQL queries
   cur = conn.cursor()
   # Execute a SELECT query to retrieve data
   cur.execute("SELECT * FROM ab_nyc_6")
   # Fetch all the rows returned by the query
   rows = cur.fetchall()
   # Iterate over the rows and print the data
   for row in rows:
      print(row)
   # Close the cursor and the connection
   cur.close()
   conn.close()
