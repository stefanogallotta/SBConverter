#!/usr/bin/env python
# Simply Red Open Systems Tech cc
# V 1.0 - CopyWrite (all) by Stefano Gallotta
# April 27 2022 - Data Import
#
#

import pandas as pd
import pyodbc

data = pd.read_csv(r'\\192.168.0.13\Temp\Converted.csv')
df = pd.DataFrame(data)

print(df)

# Server='localhost;Database=simplyred;Trusted_Connection=True;'
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=localhost;'
                      'Database=simplyred;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

# Create Table
# cursor.execute('''
# 		CREATE TABLE master (
# 			key_value int primary key,
# 			name nvarchar(50),
# 			address varchar(150),
# 			pcode varchar(10),
# 			hometel varchar(20),
# 			mobile varchar(20)
# 			)
#                ''')
# conn.commit()

# cursor.execute('''
#                 SELECT * from master
#                 ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO master (key_value, name, address, pcode, hometel, mobile)
                VALUES (?,?,?,?,?,?)
                ''',
                   row.key_value,
                   row.name,
                   row.address,
                   row.pcode,
                   row.hometel,
                   row.mobile
                   )
conn.commit()
