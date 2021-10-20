from flask import Flask, g
from flask import render_template
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

csrf = CSRFProtect()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SESSION_COOKIE_NAME'] = 'woohaen'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/woohaen?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if app.config['DEBUG']:
        app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

    '''DB INIT'''
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
        

    '''Routes INIT'''
    from .routes import base_route, auth_route

    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    '''CSRF INIT'''
    csrf.init_app(app)        


    '''REQUEST HOOK'''
    @app.before_request
    def before_request():
        g.db = db.session

    @app.teardown_request
    def teardown_request(exception):
        # db.session.close()
        if hasattr(g, 'db'):
            g.db.close()

    @app.errorhandler(404)
    def page_404(error):
        return render_template('404.html'), 404    

    return app