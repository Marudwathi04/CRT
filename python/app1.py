from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('example.db')
cur = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT
);
'''
cur.execute(create_table_query)
conn.commit()
conn.close()

@app.route('/')
def input_form():
    return render_template('input.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
    conn.commit()

    conn.close()

    return redirect('/')

@app.route('/view_users')
def view_users():
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()

    conn.close()

    return render_template('view_users.html', rows=rows)

@app.route('/delete_user', methods=['POST'])
def delete_user():
    if 'id' in request.form:
        user_id = request.form['id']
    else:
        user_id = request.form['delete_id']

    conn = sqlite3.connect('example.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

    conn.close()

    return redirect('/view_users')

@app.route('/update_user', methods=['POST'])
def update_user():
    user_id = request.form['id']
    
    # Fetch the existing user data
    conn = sqlite3.connect('example.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user_data = cur.fetchone()
    conn.close()
    
    return render_template('update_user.html', user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)

