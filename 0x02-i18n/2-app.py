#!/usr/bin/env python3
"""
    A Basic Flask app.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
        The get_locale function with the
        babel.localeselector decorator.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


def get_locale() -> str:
    """
        The locale for a web page.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index_home() -> str:
    """
        The home/index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
