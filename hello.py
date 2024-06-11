from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/aboutus/', methods=['GET'])
def aboutus():
    message = "Welcome to our page!"
    return render_template('aboutus.html', message = message)

@app.route('/privacypolicy/')
def privacypolicy():
    return render_template('privacypolicy.html')

if __name__ == '__main__':
    app.run()