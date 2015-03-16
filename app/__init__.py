
import os.path as op
from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail, Message
from flask.ext.admin import Admin, BaseView, expose, form, helpers
from flask import request, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

#from app.admin.views import MyView, MyAdminIndexView, AuthenticatedModelView, AuthenticatedFileAdmin


bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
#pagedown = PageDown()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    #pagedown.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    #admin crap
    #admin = Admin(app, 'Auth', index_view=MyAdminIndexView(), base_template='/admin/my_master.html')
    #admin.add_view(AuthenticatedModelView(User, db.session))
    #admin.add_view(AuthenticatedModelView(ipBlock, db.session))

    path = op.join(op.dirname(__file__), 'static')


    return app