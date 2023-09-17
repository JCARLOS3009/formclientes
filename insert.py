import sqlite3

conn = sqlite3.connect('cadastro.db')

c = conn.cursor()
c.execute('SELECT * FROM users')
users = c.fetchall()


c.execute('''INSERT INTO users (cliente, cnpj, marca, cidade, bairro, telefone, vendedor, data,  email) VALUES ('walter','12.345.678/0001-90','Wella','Lauro','Itinga','(11) 9999-9999','Paulo Henrique', '2023-04-10','paulo@gmail.com')''')


conn.commit()
conn.close()

print(users)

