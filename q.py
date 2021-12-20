import sqlite3
import pandas as pd
import re

con = sqlite3.connect('works.sqlite')
cursor = con.cursor()
cursor.execute('drop table if exists works')
cursor.execute('create table works ('
               'ID INTEGER PRIMARY KEY AUTOINCREMENT,'
               'salary INTEGER,'
               'educationType TEXT,'
               'jobTitle TEXT,'
               'qualification TEXT,'
               'gender TEXT,'
               'dateModify TEXT,'
               'skills TEXT,'
               'otherInfo TEXT)')
con.commit()

df = pd.read_csv("works.csv")

df.to_sql("works", con, if_exists='append', index=False)
con.commit()

cursor.execute('create index salary_index on works (salary)')
con.commit()

cursor.execute('SELECT COUNT(*) FROM works')
print(cursor.fetchall()[0][0])

cursor.execute('SELECT COUNT(*) FROM works where gender = "Мужской"')
print(cursor.fetchall()[0][0])

cursor.execute('SELECT COUNT(*) FROM works where gender = "Женский"')
print(cursor.fetchall()[0][0])

cursor.execute('SELECT COUNT(*) FROM works where skills not null')
print(cursor.fetchall()[0][0])

cursor.execute('SELECT salary FROM works where skills LIKE "%Python%"')
print(cursor.fetchall())

cursor.execute('SELECT salary FROM works where gender = "Мужской"')
man_salary = [t[0] for t in cursor.fetchall()]
print(man_salary)

cursor.execute('SELECT salary FROM works where gender = "Женский"')
w_salary = [t[0] for t in cursor.fetchall()]
print(w_salary)

plt.plot()
man_salary = np.quantile(man_salary, np.linspace(0.1, 1, 10))
w_salary = np.quantile(w_salary, np.linspace(0.1, 1, 10))

plt.hist(man_salary, bins=100, color='blue')
plt.show()
plt.hist(w_salary, bins=100, color='red')
plt.show()
