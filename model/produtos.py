from database.conexao import conectar

def select():
    conexao, cursor = conectar()
    cursor.execute('select * from produtos')
    itens = cursor.fetchall()
    conexao.close()
    return itens

