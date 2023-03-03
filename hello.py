from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!<h1>' \
           '<p>This is a paragraph.<p>' \
           '<img src="https://media.giphy.com/media/YRVP7mapl24G6RNkwJ/giphy.gif" width=200>'

@app.route("/bye")
def say_bye():
    return "Bye Bye"

@app.route("/<name>")
def greet(name):
    return f"hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)

greet()


app = Flask(__name__)


def make_bold(function):
    def wrapped_function():
        return f"<b>{function()}</b>"

    return wrapped_function


def make_emphasized(function):
    def wrapped_function():
        return f"<em>{function()}</em>"

    return wrapped_function


def make_underlined(function):
    def wrapped_function():
        return f"<u>{function()}</u>"

    return wrapped_function


@app.route('/')
def hello_world():
    return 'Main page.'


@app.route('/bye')
@make_bold
@make_underlined
@make_emphasized
def bye():
    return 'Bye'


@app.route('/<name>')
def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
