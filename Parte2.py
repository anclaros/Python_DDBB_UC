# importamos el conector
import mysql.connector as db

# creamos una conexión con el motor MySQL
mydb = db.connect(
 host = 'localhost',
 user = 'root',
 passwd = '123.Hope**',
 database = ''
)

# usando la conexión creamos un cursor
my_cursor = mydb.cursor()

# cargamos en una variable la sentencia SQL para crear la nueva base de datos
sqlsentence = 'CREATE DATABASE newDatabase'

# ejecutamos la sentencia que crea la base de datos
my_cursor.execute(sqlsentence)

# creamos una nueva conexión con la base de datos creada
mydb = db.connect(
 host = 'localhost',
 user = 'root',
 passwd = '123.Hope**',
 database = 'newDatabase'
)

# usando la conexión creamos un cursor
my_cursor = mydb.cursor()

# cargamos en una variable la sentencia SQL para crear la la tabla users
sqlSentence = 'CREATE TABLE users(name VARCHAR(45), email VARCHAR(45), \
 age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)'
# ejecutamos la sentencia que crea la tabla users
my_cursor .execute(sqlSentence)
# cargamos en una variable la sentencia SQL para agregar una fila
sqlSentence = 'INSERT INTO users(name, email, age) VALUES (%s, %s, %s)'
# cargamos en una variable la tupla
fila = ('Pepe', 'pepe@gmail.com', 25)
#ejecutamos la sentencia qye agrega la fila
my_cursor .execute(sqlSentence, fila)
# cargamos en una variable la sentencia SQL para agregar varias filas (esla misma)
sqlSentence = 'INSERT INTO users(name, email, age) VALUES (%s, %s, %s)'
# preparamos un arreglo de las tuplas a agregar
filas = [
 ('Hugo', 'hugo@gmail.com', 25),
 ('Paco', 'paco@gmail.com', 26),
 ('Luis', 'luis@gmail.com', 27)
]
# ejecutamos la sentencia que inserta las filas (notar el executemany)
my_cursor .executemany(sqlSentence, filas)
mydb.commit()