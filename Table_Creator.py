import mysql.connector

conn = mysql.connector.connect(
    host="[Your HOST]", user="[Your USER]", passwd="[Your PASS]", database="[Your DB]")
cur = conn.cursor()
cur.execute(
    "create table mydata(rollno int primary key AUTO_INCREMENT,name varchar(50),percentage float,branch varchar(10))")
conn.close()
