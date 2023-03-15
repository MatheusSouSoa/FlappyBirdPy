import mysql.connector as mysql
from tkinter import *
from flappybird import pontos





def insert ():
    nome = e_nome.get()
    pontucao = e_pontuacao.get()

    if(nome == ""):
        pass
    else:
        con = mysql.connect(host = 'localhost', user = 'root', password ='', database ='flappybird')
        cursor = con.cursor()
        cursor.execute(f"insert into pontucao values (' {pontucao}, {nome}')")
        cursor.execute('commit')
        con.close()



e_nome = Entry()
e_pontuacao = str(pontos)