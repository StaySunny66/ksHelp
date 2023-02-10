import mysql.connector

mydb = mysql.connector.connect(
    host="###################",
    user="###################",
    passwd="###################",
    database="auto"
)
mydbi = mysql.connector.connect(
    host="###################",
    user="###################",
    passwd="###################",
    database="auto"
)


def get_user():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM `user`"
    mycursor.execute(sql)
    mydb.close()

    return mycursor.fetchall()


def up_user(user, Etoken, Eid):
    mycursor = mydbi.cursor()
    user = str(user)
    cmd = "UPDATE" + '`' + 'auto' + '`' + '.`user` SET `csrftoken` = \'' + Etoken + '\', `sessionid` = \'' + Eid + '\' WHERE ''`' + 'user' + '`' + '.`' + 'school_id` = ' + user
    mycursor.execute(cmd)
    mydbi.commit()
    mycursor.fetchone()
