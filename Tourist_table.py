import mysql.connector
x=input("Enter Your Uername: ")
y=input("Enter Your Password: ")
mydb = mysql.connector.connect(
  host="localhost",
  user=x,
  password=y,
  database="Tourism"
)

mycursor = mydb.cursor()

# create tABLE
mycursor.execute("CREATE TABLE CAFETERIA (C_NO int NOT NULL AUTO_INCREMENT, Name_of_Place VARCHAR(255),ADDRESS VARCHAR(500),PHONE_NO VARCHAR(255),PRIMARY KEY (C_NO))")
s="INSERT INTO user (User_id,Password) VALUES ('" +"root" + "','" +"root"+"'"+ ")"
mycursor.execute(s)


mycursor.execute("SHOW TABLE")
"""
m=mycursor.fetchall()
print("\n \t \t Congratulations !!!!!!!!!!!!!!!!!!!!!!")
print("\t \t All required tables are Created for You")
print("\n Name of Created tables are")
for i in range(len(m)):
    print(m[i][0])
mydb.commit()



# insert into table
"""
"""for i in range(0,len(x)):
    s="INSERT INTO data (Region,Rep,item,unit) VALUES ('" +x[i] + "'," +"'"+y[i] + "'," +"'"+z[i]  +"',"+ str(k[i]) + ")"
    mycursor.execute(s)"""

