from flask import Flask, render_template
# from postgres import Postgres

app = Flask(__name__)
# db = Postgres("postgres://sammy@localhost/sammy")

def counter():
    count = 0
    while True:
        count += 1
        yield count


@app.route("/")
def hello_world():
    next(counter())
    return "<p>Hello World, pal1!</p>"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    next(counter())
    return render_template('hello.html', name=name)


@app.route('/root/')
def root():
    title = 'My super site'
    next(counter())
    return f'<html><body><h1>{title}</h1></body></html>'


@app.route('/counter/')
def counter_page():
    title = 'Counter'
    actual_count = next(counter())
    return f'<html><body><h1>Count: {actual_count}</h1></body></html>'


