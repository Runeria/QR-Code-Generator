from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def index_page() -> str:
        return 'hello world !'

    return app