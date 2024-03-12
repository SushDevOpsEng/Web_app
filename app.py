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

