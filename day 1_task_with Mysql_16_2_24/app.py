from flask import Flask, request, render_template ,redirect,session
import os
from werkzeug.utils import secure_filename
# this is for calculatin age
from dateutil.relativedelta import relativedelta
import datetime
#for encription and decription
import hashlib

import mysql.connector


#has function

hash_object = hashlib.sha256()

#data base connection
mydb = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='Student')
#mycursor = mydb.cursor()




app = Flask(__name__)

# this session key for passing the varibal one router to another , it make secure and unike
app.secret_key = 'the random string'

# image ka leya ha ya 
upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder


#main code
@app.route('/')
def home():  
    return render_template("index.html")




@app.route('/login' , methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':

        email_cheak = (request.form['email'])
        password_cheak= (request.form['password'])


            # user logi password print
        hash_object.update(password_cheak.encode())
        password_cheak = hash_object.hexdigest()

        session["email_cheak"] = email_cheak
        session["password_cheak"] = password_cheak
        
        print(password_cheak)


        # yo data base sa koi particular ak value ko uutha raha ha
        #sql_query = "SELECT *FROM `std_pannel` WHERE email ='%s' AND password ='%s'" % (email_cheak,password_cheak)
        sql_query = "SELECT *FROM `std_pannel` WHERE email ='%s' " % (email_cheak)
        mycursor.execute(sql_query)  
        myresult = mycursor.fetchall()

        # for x in myresult:
        #     print(4)
        #     print(4)
        #     print(4)

        a1=list(myresult)
        print(a1)
        # print(myresult)
        # print(len(a1))

        if len(a1) >= 1:
            print(len(a1))
            a2=a1[0][2]
            print(a2)
            print(9)
            

        #mydb.close()

        if a2 == password_cheak:
            #del a2 ,a1 ,myresult ,sql_query
            return redirect('/my_profile')
        
        else:
            return render_template("login.html"  , prediction_text="incorrect User Id or Password")
        #return password_cheak


    return render_template("login.html" ) 
  



@app.route('/registration',methods=['GET','POST'])
def registration():
    if request.method == "POST":
        # be encoded to byte string before encryption
        
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        User_Ids = request.form['User_Ids']
        password =  request.form['password']
        user_dob =  request.form['user_dob']

        image=""

        # be encoded to byte string before encryption


        hash_object.update(password.encode())
        password = hash_object.hexdigest()

                # inserting the data in the database 
        
        #sql = """INSERT INTO std_pannel (name  , email , password,  User_id,  DOB, image , mobil )  VALUES (name, email, password , user_dob , "5-5-4" ,"ff" ,"444")"""
        sql = (" INSERT INTO std_pannel (name  , email , password,  User_id,  DOB, image , mobil )"  " VALUES (%s ,%s ,%s ,%s ,%s ,%s ,%s)")
        VAL= (name,  email, password,User_Ids , user_dob ,image ,mobile)

        mycursor.execute(sql,VAL)
   
   # Commit your changes in the database
        mydb.commit()

        # try:
        # # Executing the SQL command

        #     mycursor.execute(sql)

        #     # Commit your changes in the database
        #     mydb.commit()
        #     print(7)

        # except:
        #     # Rolling back in case of error
        #     mydb.rollback()
        #     print(19)
    

        return redirect('/login')
            
    return render_template("registration.html")




@app.route('/my_profile', methods=['GET', 'POST'])
def my_profile():
    user_email=session.get("email_cheak",None)
    user_password=session.get("password_cheak",None)

    sql_query = "SELECT *FROM `std_pannel` WHERE email ='%s' AND password ='%s'" % (user_email,user_password)
    mycursor.execute(sql_query)  
    myresult = mycursor.fetchall()
    a1=list(myresult)
    # a2=a1[0][2]


   
    # for image display
    if request.method == 'POST':
        #(Update_Password)
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)

        #save the image in data base
        sql_query= "UPDATE std_pannel SET image =%s WHERE email =%s "


    # Executing query
        mycursor.execute(sql_query,(filename,user_email))  
        mydb.commit()
        

         
        #add image detail in data base


        return render_template('my_profile.html', img=img , user_name=a1[0][0] , user_mobile= a1[0][6],user_email=a1[0][1],user_User_Ids=a1[0][3], User_date=a1[0][4])
   

    if len(a1[0][5]) >5:
        return render_template('my_profile.html' , display_img=a1[0][5], user_name=a1[0][0] , user_mobile= a1[0][6],user_email=a1[0][1],user_User_Ids=a1[0][3], User_date=a1[0][4])

    else:
        return render_template('my_profile.html' , user_name=a1[0][0] , user_mobile= a1[0][6],user_email=a1[0][1],user_User_Ids=a1[0][3], User_date=a1[0][4])




# for update the student detail bt the student
@app.route('/std_updates' ,methods= ["POST" ,"GET"])
def std_updates():

    user_email=session.get("email_cheak",None)
    user_password=session.get("password_cheak",None)


    sql_query = "SELECT *FROM `std_pannel` WHERE email ='%s' AND password ='%s'" % (user_email,user_password)
    mycursor.execute(sql_query)  
    myresult = mycursor.fetchall()
    a1=list(myresult)
    Update_name = request.args.get('Update_name')

    if Update_name :

        Update_name = request.args.get('Update_name')
        print(Update_name)
        sql_query= "UPDATE std_pannel SET name =%s WHERE email =%s "


    # Executing query
        mycursor.execute(sql_query,(Update_name ,user_email))  
        mydb.commit()
        print("hello")


    return render_template("std_updates.html" ,display_img=a1[0][5], user_name=a1[0][0] , user_mobile= a1[0][6],user_email=a1[0][1],user_User_Ids=a1[0][3], User_date=a1[0][4])


# logine by the admine

@app.route('/dashboad')
def dashboad():

        
    sql_query = "SELECT *FROM `std_pannel`"
# Executing query
    mycursor.execute(sql_query)  
    myresult = mycursor.fetchall()
    x=list(myresult)
    #for calculating age

    new_data=[]
    for i1 in x:
        c=i1[4]

        birthdate = datetime.datetime.strptime( str(c), '%Y-%m-%d').date()
        today = datetime.date.today()
        age = relativedelta(today, birthdate).years
        i1=list(i1)
        i1.append(age)

        i1=tuple(i1)
        new_data.append(i1)

    print(new_data)

    return render_template("dashboad.html" , all_data=new_data)



@app.route('/admine_update')# ,methods=['POST','GET'])
def admine_update():


   
    return render_template("admine_update.html" )


if __name__=="__main__":
  app.run(debug=True)