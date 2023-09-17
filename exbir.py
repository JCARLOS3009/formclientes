import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('cadastro.db')

    cur = conn.cursor()
    cur.execute('SELECT * FROM cadastro')
    users = cur.fetchall()
    
    rows = [dict(row) for row in cur.fetchall()]
    with open('nome_do_arquivo.json', 'w') as f:
      json.dump(rows, f)
    conn.close()
    print(users)