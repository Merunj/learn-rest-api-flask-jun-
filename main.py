from data import db_session
from flask import Flask
import data.user_api as user_api

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/db_flask.db")
    app.register_blueprint(user_api.blueprint)
    app.run(debug=True)


if __name__ == '__main__':
    main()    