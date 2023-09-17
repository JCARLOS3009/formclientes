import sqlite3

conn = sqlite3.connect('cadastro.db')

c = conn.cursor()

c.execute('''CREATE TABLE users
             (cliente text,cnpj text, marca text, cidade text, bairro text, telefone text, vendedor text, data text,  npedido text, observacao text);''')
conn.commit()
conn.close()
