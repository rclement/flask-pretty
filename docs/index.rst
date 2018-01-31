Flask-Pretty
============

.. toctree::
    :maxdepth: 2
    :caption: Contents:

.. module:: flask_pretty

Flask-Pretty is a Flask extension to output prettified HTML pages to ease the
development process of HTML templates.
However, HTML prettifying should only be used for development purposes only.
For production purposes, HTML minifying should be used instead (for instance by using Flask-HTMLmin_).

The underlying HTML prettifying process is provided by BeautifulSoup_.

.. _Flask-HTMLmin: https://github.com/hamidfzm/Flask-HTMLmin
.. _BeautifulSoup: https://www.crummy.com/software/BeautifulSoup

Installation
------------

Install the extension with with pipenv_ (recommended)::

    $ pipenv install flask-pretty

Or with pip_::

    $ pip install flask-pretty

.. _pip: https://pip.pypa.io
.. _pipenv: https://docs.pipenv.org

Usage
-----

Using Flask-Pretty is really simple:

.. code-block:: python

    import Flask
    from flask_pretty import Prettify

    app = Flask(__name__)
    prettify = Prettify(app)

Or if you are using the Flask `Application Factories`_ pattern:

.. code-block:: python

    import Flask
    from flask_pretty import Prettify

    prettify = Prettify()

    def create_app():
        app = Flask(__name__)
        prettify.init_app(app)

Flask-Pretty is configurable via the following configuration variables:

- `PRETTIFY`: enable Flask-Pretty for all routes (default: False)

.. _Application Factories: http://flask.pocoo.org/docs/0.12/patterns/appfactories/

API
---

.. autoclass:: flask_pretty.Prettify
    :members:
