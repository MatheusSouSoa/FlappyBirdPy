import sqlite3


def table():
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute('create table record(id integer,ponto integer)')
    con.commit()


def selectPoint():
    point = 0
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("select ponto from record where id = 1 ")
    rows= cursor.fetchall()
    
    for i in rows:
        point = i[0]
        
    con.close()

    return point

def newRecord(pontos):
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute(f'update record set ponto = {pontos} where id = 1')
    con.commit()
    con.close()

def startInsert():#v
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute(f'select count(*) from record')
    for i in cursor:
        cmp = i[0]

    if(cmp == 0):
        cursor.execute('insert into record values (1,0)')
        con.commit()
    con.close()

