import os

from flask import Flask
from flask import current_app



def create_app():
    app =Flask(__name__)#initialising Flask
    app.config['SECRET_KEY']='TesT'#encrypts Data

    from .ame import ame
    app.register_blueprint(ame, url_prefix='/')

    from .space import space
    app.register_blueprint(space, url_prefix='/')

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    from .lore import lore
    app.register_blueprint(lore, url_prefix='/')





    return app

app = create_app()

if __name__=='__main__':
    app.run(debug="True")