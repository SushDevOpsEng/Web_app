# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample list of items
items = ["Item 1", "Item 2", "Item 3"]

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    new_item = request.form['item']
    items.append(new_item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

python
Copy code
# app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample list of items
items = ["Item 1", "Item 2", "Item 3"]

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    new_item = request.form['item']
    items.append(new_item)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
html
Copy code
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Web Application</title>
</head>
<body>
    <h1>Simple Web Application</h1>
    <h2>Items:</h2>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
    <h2>Add New Item:</h2>
    <form action="/add" method="post">
        <input type="text" name="item" placeholder="Enter item">
        <button type="submit">Add</button>
    </form>
</body>
</html>

