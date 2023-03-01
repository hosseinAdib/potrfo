from flask import Flask, render_template, send_from_directory, request
from jinja2 import TemplateNotFound
import csv
from app import app as application

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page>')
def show(page=''):
    try:
        return render_template(f'{page}')
    except TemplateNotFound:
        return render_template('404.html'), 404 


@app.route('/', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            email = data['email']
            name = data['name']
            with open('data.csv', newline='',mode='a') as csvform:
                writer = csv.writer(csvform, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([email, name])
        except:
            return 'Smth didnt save to database'
        return render_template('/index.html')

    else:
        return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)

