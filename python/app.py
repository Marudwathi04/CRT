from flask import Flask
app=Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to our Product Management System</h1>
    <ul>
        <li><a href="/add_product">Add Product</a></li>
        <li><a href="/remove_product">Remove Product</a></li>
        <li><a href="/view_product">View Product</a></li>
    </ul>
</body>
</html> 
"""
@app.route('/addproduct')
def add():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product</title>
</head>
<body>
    <h1>Add Product</h1>
    <!-- Your add product form goes here -->
    <form action="/add_product" method="post">
        <!-- Form fields for adding product -->
    </form>
</body>
</html>


"""
@app.route('/viewproduct')
def view():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Product</title>
</head>
<body>
    <h1>View Product</h1>
    <!-- Your product list or details display goes here -->
</body>
</html>
"""
@app.route('/removeproduct')
def remove():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Remove Product</title>
</head>
<body>
    <h1>Remove Product</h1>
    <!-- Your remove product form or list goes here -->
    <form action="/remove_product" method="post">
        <!-- Form fields or list items for removing product -->
    </form>
</body>
</html>

"""
if __name__=="__main__":
    app.run(debug=True)