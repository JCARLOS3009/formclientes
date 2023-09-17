import os 
print(os.listdir())


import sqlite3
conn = sqlite3.connect('test3.db')
print("Opened database successfully")



print(os.listdir())




conn.execute("DROP TABLE IF EXISTS COMPANY")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
         
print("Table created successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'Cali-fornia', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print("Records created successfully")


print("Total number of rows updated :", conn.total_changes)







cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")








conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 2")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Total number of rows updated :", conn.total_changes)
   
   
   
   
   
   
   
   
conn.execute("DELETE from COMPANY where ID = 2;")
conn.commit()
print("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")







cursor = conn.execute("SELECT * FROM COMPANY WHERE ADDRESS  LIKE '%-%';")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3], "\n")

print("Operation done successfully")
conn.close()


#Like: Types of clauses
#1) WHERE SALARY LIKE '200%' - Finds any values that start with 200

#2)	WHERE SALARY LIKE '%200%' - Finds any values that have 200 in any position

#3)	WHERE SALARY LIKE '_00%' - Finds any values that have 00 in the second and third positions

#4)	WHERE SALARY LIKE '2_%_%' - Finds any values that start with 2 and are at least 3 characters in length

#5)	WHERE SALARY LIKE '%2' - Finds any values that end with 2

#6)	WHERE SALARY LIKE '_2%3' - Finds any values that has a 2 in the second position and ends with a 3

#7)	WHERE SALARY LIKE '2___3' - Finds any values in a five-digit number that starts with 2 and ends with 3










