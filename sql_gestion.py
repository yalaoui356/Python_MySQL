#Import the mysql connector
import mysql.connector

#   connect to my Database
mydb = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'JU19vx44$', database = 'Tutorat')

# creat cursor
mycursor = mydb.cursor()

# show databases
mycursor.execute('select * from student')
result = mycursor.fetchall()

# Display table (Tuple)
for i in result:
    print(i)
    print('Ajout age...')
    i += ('40 ans',)
    print(i)
    print('****************************'
          '***************************')

result = mycursor.fetchall()
for j in result:
    print(j)

