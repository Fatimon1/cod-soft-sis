import sqlite3
from DataBaseManager import DataBaseManager

dataBaseManager = DataBaseManager()


con = sqlite3.connect(dataBaseManager.database)
materia = (12,'matematicas', 'Soto Hernandez Erick Otoniel', 9)
if not dataBaseManager.is_an_existing_materia(con, materia):
    dataBaseManager.create_materia(con, materia)


materia = (8,'matematicas', 'Soto Hernandez Erick Otoniel', 12)
dataBaseManager.update_materia(con, materia)
cur = con.cursor()
cur.execute("Select * from materias;")
table_list = cur.fetchall()
for row in table_list:
    print(row)
con.close()