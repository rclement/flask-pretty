# Flask-Pretty

[![PyPI Version](https://img.shields.io/pypi/v/flask-pretty.svg)](https://pypi.python.org/pypi/flask-pretty)
[![PyPI License](https://img.shields.io/pypi/l/flask-pretty.svg)](https://pypi.python.org/pypi/flask-pretty)
[![PyPI Versions](https://img.shields.io/pypi/pyversions/flask-pretty.svg)](https://pypi.python.org/pypi/flask-pretty)
[![Build Status](https://travis-ci.org/rclement/flask-pretty.svg?branch=master)](https://travis-ci.org/rclement/flask-pretty)
[![Coverage Status](https://coveralls.io/repos/github/rclement/flask-pretty/badge.svg?branch=master)](https://coveralls.io/github/rclement/flask-pretty?branch=master)
[![Documentation Status](https://readthedocs.org/projects/flask-pretty/badge/?version=master)](http://flask-pretty.readthedocs.io/en/master/)

Flask-Pretty is a [Flask](http://flask.pocoo.org) extension to output prettified
HTML pages to ease the development process of HTML templates.
However, HTML prettifying should only be used for development purposes only.
For production purposes, HTML minifying should be used instead
(for instance by using [Flask-HTMLmin](https://github.com/hamidfzm/Flask-HTMLmin)).

The underlying HTML prettifying process is provided by [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup).

## Installation

Install the extension with with [pipenv](https://docs.pipenv.org) (recommended):

    $ pipenv install flask-pretty

Or with [pip](https://pip.pypa.io):

    $ pip install flask-pretty

## Usage

Using Flask-Pretty is really simple:

```
    import Flask
    from flask_pretty import Prettify

    app = Flask(__name__)
    prettify = Prettify(app)
```

## Documentation

The Sphinx-compiled documentation is available on [ReadTheDocs](http://flask-pretty.readthedocs.io/en/latest/).

## License

The MIT License (MIT)

Copyright (c) 2018 Romain Clement
