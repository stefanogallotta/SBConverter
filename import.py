#!/usr/bin/python
# Simply Red Open Systems Tech cc
# V 1.0 - CopyWrite (all) by Stefano Gallotta
# Apr 29th 2022 Python SB Convert
# ICanDoThis
# Dict extraction
#
# Create/Import DB frmo CSV files ex D3

import pandas as pd
import pyodbc
import SBOpenMySQL			# "secure" open MySQL (mine!)

data = pd.read_csv (r'\\192.168.0.13\Temp\Converted.csv')
df = pd.DataFrame(data)

# print(df)

# Server='localhost;Database=simplyred;Trusted_Connection=True;'
# conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
#                       'Server=localhost;'
#                       'Database=simplyred;'
#                       'Trusted_Connection=yes;')
# cursor = conn.cursor()
conn      = SBOpenMySQL.SQLMSOpen('')
cursor  = conn.cursor()

#
# # Create Table Products
# cursor.execute('''
# 		CREATE TABLE products (
# 			key_value int ,
# 			description varchar(30),
# 			qty varchar(10),
# 			unitprice varchar(10)
# 			)
#                ''')
# conn.commit()
# print('table products created')

# Create Data for products

# Insert DataFrame to Table
# for row in df.itertuples():
#     cursor.execute('''
#                 INSERT INTO products (key_value, description, qty, unitprice)
#                 VALUES (?,?,?,?)
#                 ''',
#                 row.stockno,
#                 row.description,
#                 row.qty,
#                 row.unitprice
#                 )
# conn.commit()
# print('data inserted for products')
# cursor.execute('''
#                 SELECT * from products
#                 ''')
# conn.commit()

# Create Table master

cursor.execute('''
		CREATE TABLE master (
			key_value varchar(10),
			name varchar(30),
			address varchar(100),
			pcode varchar(10),
			hometel varchar(14),
			mobiletel varchar(14)
			)
               ''')
conn.commit()
print('table master created')

# Create Data for master
cursor.execute('''
                SELECT * from master
                ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO master (key_value, name, address, pcode, hometel, mobiletel)
                VALUES (?,?,?,?,?,?)
                ''',
                row.key,
                row.name,
                row.address,
                row.pcode,
                row.hometel,
                row.mobiletel
                )
conn.commit()
print('data inserted for master')
