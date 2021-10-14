import mysql.connector as db
from mysql.connector import Error

try:
    mydb = db.connect( #se crea la conexión
        host = "localhost",
        user = "ayudante", #cambiar a root
        passwd = "12345", #colocar su contraseña
        database = "ayudantes10"
    )
    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        my_cursor = mydb.cursor()

        sqlsentence1 = "CREATE TABLE ayudantes(rut VARCHAR(12) PRIMARY KEY NOT NULL, \
                nombre VARCHAR(20), carrera INT, \
                FOREIGN KEY (carrera) REFERENCES carreras(id_carrera))"

        sqlsentence2 = "CREATE TABLE carreras(id_carrera INT NOT NULL AUTO_INCREMENT PRIMARY KEY , \
                        nombre VARCHAR(25))"
        my_cursor.execute(sqlsentence2)
        my_cursor.execute(sqlsentence1)
        
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (mydb.is_connected()):
        my_cursor.close()
        mydb.close()
        print("MySQL connection is closed")