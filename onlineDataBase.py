import mysql.connector as mysql

def criacao():
    con = mysql.connect(host = 'localhost', user = 'root', password ='')
    cursor = con.cursor()
    cursor.execute(f"create database if not exists flappybird")
    cursor.execute('commit')
    con.close()

def tabela():
    con = mysql.connect(host = 'localhost', user = 'root', password ='',database='flappybird ')
    cursor = con.cursor()
    cursor.execute('create table if not exists record(\
                        id int primary key auto_increment,\
                        ponto int(3)\
    )')
    cursor.execute('commit')
    con.close
    con=mysql.connect(host='localhost',user='root',password='',database='flappybird')
    cursor = con.cursor()

def select():
    point = 0
    con=mysql.connect(host='localhost',user='root',password='',database='flappybird')
    cursor = con.cursor()
    cursor.execute("select ponto from record where id = 1 ")
    rows= cursor.fetchall()
    
    for i in rows:
        point = i[0]
        
    con.close()

    return point

def novoRecorde(pontos):
    con=mysql.connect(host='localhost',user='root',password='',database='flappybird')
    cursor = con.cursor()
    cursor.execute(f'update record set ponto = {pontos} where id = 1')
    cursor.execute("commit")
    con.close()

def startIns():
    con=mysql.connect(host='localhost',user='root',password='',database='flappybird')
    cursor = con.cursor()
    cursor.execute(f'select count(*) from record')
    for i in cursor:
        cmp = i[0]

    if(cmp == 0):
        cursor.execute('insert into record (ponto) value (0)')
        cursor.execute('commit')
    con.close()