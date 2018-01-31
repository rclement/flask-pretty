Flask-Pretty
============

|PyPI Version| |PyPI License| |PyPI Versions| |Build Status| |Coverage
Status| |Documentation Status|

Flask-Pretty is a `Flask <http://flask.pocoo.org>`__ extension to output
prettified HTML pages to ease the development process of HTML templates.
However, HTML prettifying should only be used for development purposes
only. For production purposes, HTML minifying should be used instead
(for instance by using
`Flask-HTMLmin <https://github.com/hamidfzm/Flask-HTMLmin>`__).

The underlying HTML prettifying process is provided by
`BeautifulSoup <https://www.crummy.com/software/BeautifulSoup>`__.

Installation
------------

Install the extension with with `pipenv <https://docs.pipenv.org>`__
(recommended):

::

    $ pipenv install flask-pretty

Or with `pip <https://pip.pypa.io>`__:

::

    $ pip install flask-pretty

Usage
-----

Using Flask-Pretty is really simple:

::

        import Flask
        from flask_pretty import Prettify

        app = Flask(__name__)
        prettify = Prettify(app)

Documentation
-------------

The Sphinx-compiled documentation is available on
`ReadTheDocs <http://flask-pretty.readthedocs.io/en/latest/>`__.

License
-------

The MIT License (MIT)

Copyright (c) 2018 Romain Clement

.. |PyPI Version| image:: https://img.shields.io/pypi/v/flask-pretty.svg
   :target: https://pypi.python.org/pypi/flask-pretty
.. |PyPI License| image:: https://img.shields.io/pypi/l/flask-pretty.svg
   :target: https://pypi.python.org/pypi/flask-pretty
.. |PyPI Versions| image:: https://img.shields.io/pypi/pyversions/flask-pretty.svg
   :target: https://pypi.python.org/pypi/flask-pretty
.. |Build Status| image:: https://travis-ci.org/rclement/flask-pretty.svg?branch=master
   :target: https://travis-ci.org/rclement/flask-pretty
.. |Coverage Status| image:: https://coveralls.io/repos/github/rclement/flask-pretty/badge.svg?branch=master
   :target: https://coveralls.io/github/rclement/flask-pretty?branch=master
.. |Documentation Status| image:: https://readthedocs.org/projects/flask-pretty/badge/?version=master
   :target: http://flask-pretty.readthedocs.io/en/master/
