import sqlite3
from pathlib import Path

connection = sqlite3.connect(Path.home()/ Path('Desktop', 'Data_Base.db'))
crsr = connection.cursor()
print('connected to the database')


# انشاء جدول في قاعدة البيانات
sql_command = """CREATE TABLE if not exists students (
first_name VARCHAR(20),
last_name VARCHAR(20), 
age INTEGER)"""

crsr.execute(sql_command)

#insert data
crsr.execute('INSERT INTO students VALUES ("hadi", "hasen" , 23);')
crsr.execute('INSERT INTO students VALUES ("norah", "nh" , 23);')
crsr.execute('INSERT INTO students VALUES ("nh", "hf" , 23);')

connection.commit()

# اغلاق قاعدة البيانات
connection.close()

