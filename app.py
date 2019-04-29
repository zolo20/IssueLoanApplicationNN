from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import POSTGRES
from eureka import eureka

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from request import training
from controller import predict

#db.create_all() FOR CREATE A NEW DATA BASE
eureka()
training()


if __name__ == '__main__':
    app.run()
