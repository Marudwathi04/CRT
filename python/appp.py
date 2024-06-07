from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize the database and create the Products table if it doesn't exist
def init_db():
    conn = sqlite3.connect('products.db')
    cur = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL,
        description TEXT
    );
    '''
    cur.execute(create_table_query)
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def input_form():
    return render_template('index.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        
        conn = sqlite3.connect('products.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO products (name, price, description) VALUES (?, ?, ?)", (name, price, description))
        conn.commit()
        conn.close()
        
        return redirect('/')
    return render_template('add_product.html')

@app.route('/view_products')
def view_products():
    conn = sqlite3.connect('products.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    conn.close()
    return render_template('view_products.html', rows=rows)

@app.route('/delete_product', methods=['POST'])
def delete_product():
    product_id = request.form['id']
    
    conn = sqlite3.connect('products.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    
    return redirect('/view_products')

@app.route('/update_product', methods=['POST'])
def update_product():
    product_id = request.form['id']
    
    # Fetch the existing product data
    conn = sqlite3.connect('products.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product_data = cur.fetchone()
    conn.close()
    
    return render_template('update_product.html', product_data=product_data)

if __name__ == '__main__':
    app.run(debug=True)
