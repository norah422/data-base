import sqlite3
from pathlib import Path

connection2 = sqlite3.connect(Path.home()/ Path('Desktop', 'Data_Base.db'))
crsr = connection2.cursor()
print('connected to the database')

crsr.execute('SELECT name,salary FROM employees where salary > 800')
#print(crsr.fetchall())
#print(crsr.fetchone())
#print(crsr.fetchmany(3))

answer = crsr.fetchall()
for i in answer:
    print(i)




