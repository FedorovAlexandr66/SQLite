import sqlite3
import pandas as pd
import re

def get_clean_field(field):
    return re.sub(r'\<[^>]*\>', '', str(field))

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

df['skills'] = df['skills'].apply(get_clean_field)
df['otherInfo'] = df['otherInfo'].apply(get_clean_field)
