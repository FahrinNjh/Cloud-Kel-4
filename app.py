from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Web():
    return render_template('Web.html')


if __name__ == '__main__':
    app.run(debug=True)
