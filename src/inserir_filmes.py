import sqlite3
from idlelib.undo import InsertCommand

#criando banco de dados
con = sqlite3.connect("filmes.db")

#cursor no bando de dados
cur = con.cursor()

#criando tabelas
#cur.execute("CREATE TABLE filmes(Titulo, Genero, Ano de Lançamento)")

#adicionando filmes nas tabelas
cur.execute("""
    INSERT INTO filmes VALUES 
        ('Harry Potter e o Cálice de Fogo', 'Fantasia/Aventura', 2005),
        ('Harry Potter e a Ordem da Fênix', 'Fantasia/Aventura', 2007),
        ('Harry Potter e o Enigma do Príncipe', 'Fantasia/Aventura/Drama', 2009),
        ('Harry Potter e as Relíquias da Morte – Parte 1', 'Fantasia/Aventura', 2010),
        ('Harry Potter e as Relíquias da Morte – Parte 2', 'Fantasia/Aventura', 2011)
""")


# Confirma (salva) as alterações no banco
con.commit()
con.close()  # fecha a conexão com o banco
