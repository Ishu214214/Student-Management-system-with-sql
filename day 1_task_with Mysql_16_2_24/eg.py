import mysql.connector
mydb = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='Student')

mycursor = mydb.cursor()


                               # creat the data base

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Student")


                              # to show all the data base

# mycursor = mydb.cursor()
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)


                            # create the table
#mycursor.execute("CREATE TABLE student_pannels (`name` VARCHAR(15) NOT NULL , `email` VARCHAR(20) NOT NULL , `password` VARCHAR(30) NOT NULL , `User_id` INT(10) NOT NULL ))")

#CREATE TABLE `Student`.`std_pannel` (`name` VARCHAR(15) NOT NULL , `email` VARCHAR(20) NOT NULL , `password` VARCHAR(30) NOT NULL , `User_id` INT(10) NOT NULL , `DOB` DATE NOT NULL , `image` VARCHAR(50) NOT NULL , `mobil` VARCHAR(15) NOT NULL ) 


                                   # Preparing SQL query to INSERT a record into the database.


#sql = """INSERT INTO std_pannel (name  , email , password,  User_id,  DOB, image , mobil )  VALUES ('qq', 'qqqq', 'qqq','3' , "5-5-4" ,"ff" ,"444")"""

# a=3
# sql = (" INSERT INTO std_pannel (name  , email , password,  User_id,  DOB, image , mobil )"  " VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s)")
# VAL= ('qq', 'qqqq', 'qqq','3' , "5-5-4" ,"ff" ,a)

# mycursor.execute(sql,VAL)
   
#    # Commit your changes in the database
# mydb.commit()
# print(6)






# # sql = "select * from std_pannel where User_id >= 3 A;"

# # sql="SELECT * FROM `std_pannel` WHERE `email` LIKE '2020pice@gmail.com' AND `User_id` = 11"

# a="ishukr888@gmail.com"

# b="hello world"
# sql_query= "UPDATE std_pannel SET name =%s WHERE email =%s "


# # Executing query
# mycursor.execute(sql_query,(b,a))  
# mydb.commit()

# # myresult = mycursor.fetchall()
# # a=list(myresult)

# # for x in a:
# #     print(x)



   





# a="ishukr888@gmail.com"

# b='11'
# sql_query= "UPDATE `std_pannel` SET name =%s WHERE email =%s " % (b,a) 
# # Executing query
# mycursor.execute(sql_query)  
# myresult = mycursor.fetchall()

from dateutil.relativedelta import relativedelta
import datetime

sql_query = "select * from std_pannel where DOB >= 0005-05-04 "
mycursor.execute(sql_query)  
myresult = mycursor.fetchall()
a=list(myresult)
data_list=[]
age_list=[]
for x in a:
    c=x[4]
    data_list.append(c)

for i in range(0,len(data_list)):
    birthdate = datetime.datetime.strptime( str(data_list[i]), '%Y-%m-%d').date()
    today = datetime.date.today()
    age = relativedelta(today, birthdate).years
    age_list.append(age)



print(age_list)
#                      # Closing the connection


mydb.close()
