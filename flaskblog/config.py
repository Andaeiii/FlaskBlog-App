
import secrets

class Config:

    SECRET_KEY = secrets.token_hex(18) 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mysite.db'  

    #CONFIGURE MAIL.. 
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    DEBUG = True

    # # Flask-Security Config
    # app.config['SECURITY_REGISTERABLE = True
    # app.config['SECURITY_TRACKABLE = True
    # app.config['SECURITY_CONFIRMABLE = True
    # app.config['SECURITY_RECOVERABLE = True
    # SECURITY_EMAIL_SENDER = 'andaeiii@gmail.com'

    MAIL_DEFAULT_SENDER = 'andaeiii@gmail.com'
    MAIL_USERNAME = 'andaeiii@gmail.com'
    MAIL_PASSWORED = 'WYCLEF1234'