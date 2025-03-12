from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    #Load the models
    from models import db
    from models.todo import Todo
    db.init_app(app)

    #create the database tables
    with app.app_context():
        db.create_all()
        db.session.commit()
    #Register the blueprints
    from todo.views.routes import api
    app.register_blueprint(api)

    return app