from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html', currentPage='index')

@app.route('/award.html')
def award():
    return render_template('award.html', currentPage='award')

if __name__ == '__main__':
    app.run(debug=True)
