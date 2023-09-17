from flask import Flask, request, render_template,redirect, url_for
import sqlite3
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    cliente = request.form['cliente']
    cnpj = request.form['cnpj']
    marca = request.form['marca']
    cidade = request.form['cidade']
    bairro = request.form['bairro']
    telefone = request.form['telefone']
    vendedor = request.form['vendedor']
    data = request.form['data']
    npedido = request.form['npedido']
    observacao = request.form['observacao']

    conn = sqlite3.connect('cadastro.db')
    conn.execute('INSERT INTO users (cliente, cnpj, marca, cidade, bairro, telefone, vendedor, data, npedido, observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 (cliente, cnpj, marca, cidade, bairro, telefone, vendedor, data, npedido, observacao))
    conn.commit()
    conn.close()

    return redirect(url_for('listar'))
  
@app.route('/editar/<string:usernpedido>', methods=['GET'])
def edit_user(usernpedido):
    conn = sqlite3.connect('cadastro.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE npedido=?", (usernpedido,))
    user = c.fetchone()
    conn.close()

    if not user:
        return "Usuário não encontrado"

    return render_template('edit_user.html', user=user)

@app.route('/editar/<string:usernpedido>', methods=['POST'])
def update_user(usernpedido):
    conn = sqlite3.connect('cadastro.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE npedido=?", (usernpedido,))
    user = c.fetchone()

    if not user:
        return "Usuário não encontrado"

    cliente = request.form['cliente']
    cnpj = request.form['cnpj']
    marca = request.form['marca']
    cidade = request.form['cidade']
    bairro = request.form['bairro']
    telefone = request.form['telefone']
    vendedor = request.form['vendedor']
    data = request.form['data']
    npedido = request.form['npedido']
    observacao = request.form['observacao']

    c.execute("UPDATE users SET cliente=?, cnpj=?, marca=?, cidade=?, bairro=?, telefone=?, vendedor=?, data=?, npedido=?, observacao=? WHERE npedido=?", 
              (cliente, cnpj, marca, cidade, bairro, telefone, vendedor, data, npedido, observacao, usernpedido))
    
    conn.commit()
    conn.close()

    return redirect(url_for('listar'))

@app.route('/apagar/<string:usernpedido>', methods=['GET'])
def delete_user(usernpedido):
    conn = sqlite3.connect('cadastro.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE npedido=?", (usernpedido,))
    user = c.fetchone()

    if not user:
        return "Usuário não encontrado"

    c.execute("DELETE FROM users WHERE npedido=?", (usernpedido,))
    conn.commit()
    conn.close()

    return redirect(url_for('listar'))

@app.route('/users')
def users():
    conn = sqlite3.connect('cadastro.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    
    rows = [dict(row) for row in cur.fetchall()]
    with open('nome_do_arquivo.json', 'w') as f:
      json.dump(rows, f)
    conn.close()
    print(users)
    return 'exibir cadastros'
@app.route('/listar')
def listar():
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('listar.html', users=users)
@app.route('/adminlistar')
def adminlistar():
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return render_template('adminlistar.html', users=users)

app.run(host='0.0.0.0', port=81)
