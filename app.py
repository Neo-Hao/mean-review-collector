from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/<page_name>')
def other_page(page_name):
    response = make_response(render_template('404.html'), 404)
    return response

if __name__ == '__main__':
    app.run(debug=True)
