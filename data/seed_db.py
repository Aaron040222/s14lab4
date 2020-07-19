# Import csv to postgresql db

import psycopg2
import pandas as pd

conn = psycopg2.connect("host=ec2-34-198-243-120.compute-1.amazonaws.com dbname=d4iftedi2ta10k user=qisnlgixfeswvw password=d1e4642f049d845c8a26a0d7c9a47d8d9461625cf47ade64239c193b0d9a707b")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS homework_users;")

cur.execute('''CREATE TABLE homework_users (
    uid SERIAL PRIMARY KEY NOT NULL,
    username TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    prog_lang TEXT NOT NULL,
    experience_yr FLOAT NOT NULL,
    age INTEGER NOT NULL,
    hw1_hrs FLOAT NOT NULL);''')

conn.commit()

df_users = pd.read_csv('./data/predefined_users.csv', index_col=0)
for idx, u in df_users.iterrows():

    # Data cleaning

    q = cur.execute(
        '''INSERT INTO homework_users (username, first_name, last_name, prog_lang, experience_yr, age, hw1_hrs) VALUES (%s,%s,%s,%s,%s,%s,%s)''',
        (u.username, u.first_name, u.last_name, u.prog_lang, u.experience_yr, u.age, u.hw1_hrs)
    )
    conn.commit()

cur.close()
conn.close()
