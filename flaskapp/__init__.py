import os

from flask import Flask


def create_app(test_config=None):
    # создаем и настраиваем приложение
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # загружаем конфиг экземпляра приложения, если он существует
        app.config.from_pyfile('config.py', silent=True)
    else:
        # иначе загрузить тестовый конфиг
        app.config.from_mapping(test_config)

    # проверка, есть ли вообще папка экземпляра приложения
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # простая страничка (подробнее в предыдущей части статьи)
    @app.route('/wakeup')
    def wake_up():
        return 'Wake up, Neo...'

    return app