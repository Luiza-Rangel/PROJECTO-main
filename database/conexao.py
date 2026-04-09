import mysql.connector


def conectar():
        mydb = mysql.connector.connect(
                                        host="localhost",
                                        port =3306,
                                        user="root",
                                        password="root",
                                        database="db_burguer" 
                                        )
        
        cursor = mydb.cursor(dictionary=True)
        return mydb, cursor
