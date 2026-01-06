import sqlite3
from pathlib import Path

db_path = sqlite3.connect(Path.home()/ Path('Desktop', 'Data_Base.db'))
cursor2 = db_path.cursor()
print('connected to the database')

#update
cursor2.execute('UPDATE employees SET Salary = 600 WHERE id=2')

#deleting
cursor2.execute('DELETE FROM employees WHERE id = 1')

db_path.commit()
db_path.close()


