from cgi import print_exception
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'This Works'

@app.route('/inventory')
def stock():
    stocks = {
        "stock1": [
            {
                'name': 'healing potion',
                'qty': 5,
                'price': 200  
            },
            {
                'name': 'speed potion',
                'qty': 3,
                'price': 300    
            },
            {
                'name': 'gold potion',
                'qty': 1,
                'price': 2000  
            }
        ]
    }
    return stocks