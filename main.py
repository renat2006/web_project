import random

import requests
from bs4 import BeautifulSoup
import re

from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index():
    reg = re.compile('[^а-яА-Я ]')

    url = 'https://www.healthwaters.ru/blog/aforizmy-i-vyskazyvaniya-velikikh-o-zdorove/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('blockquote')
    s = random.choice(quotes).text
    quote1 = reg.sub('', s).split('   ')
    return render_template('index.html', quote=quote1[0])


if __name__ == '__main__':
    app.run(port='8080', host='127.0.0.1')
