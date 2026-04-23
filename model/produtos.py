from database.conexao import conectar

def mostrar_comidas():
    conexao, cursor = conectar()

    #executado consulta genero
    cursor.execute("SELECT codigo, produto, descricao, destaque, preco, foto FROM produtos;")

    #recuperando os dados do genero
    item = cursor.fetchall()

    #Fechando
    conexao.close()

    return item

def rec_destaque():
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT codigo, produto, descricao, destaque, preco, foto WHERE destaque =1; """)
    destaque = cursor.fetchall()
    conexao.close()
    return destaque