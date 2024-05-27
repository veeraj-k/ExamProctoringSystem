import mysql.connector
def upload_sql(usn,name,subject,login_time,logout_time,score):
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='2004',database='examps')
    cm='INSERT INTO exam(usn,name,test,login_time,score,logout_time) VALUES (%s, %s,%s,%s,%s,%s)'
    d=(usn,name,subject,login_time,score,logout_time)
    cur=mycon.cursor()
    cur.execute(cm,d)
    mycon.commit()