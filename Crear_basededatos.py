import mysql.connector as db
from mysql.connector import Error

try:
    mydb = db.connect( #se crea la conexión
        host = "localhost",
        user = "ayudante", #cambiar a root
        passwd = "12345", #colocar su contraseña
        database = ""
    )
    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        my_cursor = mydb.cursor()
        sqlsentence = 'CREATE DATABASE ayudantes10'
        my_cursor.execute(sqlsentence)
        
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (mydb.is_connected()):
        my_cursor.close()
        mydb.close()
        print("MySQL connection is closed")