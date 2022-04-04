from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret key'

    from .select import select
    from .insert import insert
    from .update import update
    from .delete import delete

    app.register_blueprint(select, url_prefix = '/select')
    app.register_blueprint(insert, url_prefix = '/insert')
    app.register_blueprint(update, url_prefix = '/update')
    app.register_blueprint(delete, url_prefix = '/delete')

    @app.route('/')
    def basicRoute():
        return redirect(url_for('select.sWarehouse'))

    return app