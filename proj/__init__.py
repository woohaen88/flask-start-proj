from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'hello_world'

    '''Routing Practice'''
    from flask import jsonify, redirect, url_for

    @app.route('/test/name/<name>')
    def name(name):
        return f'Name is {name}'

    @app.route('/test/id/<int:id>')
    def id(id):
        return f'ID: {id:d}'

    @app.route('/test/path/<path:subpath>')
    def path(subpath):
        return subpath

    @app.route('/test/json')
    def json():
        return jsonify({'hello': 'world'})

    return app 