# db_utils.py
# this file should handel queries form MySQL database
import mysql.connector
from mysql.connector import errors
# connect to the MySQL database using Flask app config
def get_db_connection(app):
    try:
        connection = mysql.connector.connect(
            host=app.config['DB_HOST'],
            user=app.config['DB_USER'],
            password=app.config['DB_PASSWORD'],
            database=app.config['DB_NAME']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
