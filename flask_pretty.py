"""
    flask_pretty
    ------------

    Flask-Pretty is a Flask extension to output prettified HTML pages to ease
    the development process of HTML templates.

    :copyright: (c) 2018 by Romain Clement
    :license: MIT, see LICENSE for more details.
"""


from bs4 import BeautifulSoup


class Prettify(object):
    """
    Primary class container for HTML pages prettifying.

    After each request, if the route is returning an HTML page, it will be
    minified using `BeautifulSoup.prettify` feature.


    You can initialize :class:`Prettify` like this::

        prettify = Prettify()

    Then pass the application object to be configured::

        prettify.init_app(app)

    You must explicitly enable Flask-Pretty by setting `PRETTIFY` to True when
    necessary (e.g. in development mode only).
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Initializes a Flask object `app`: binds the HTML prettifying with
        app.after_request.

        :param app: The Flask application object.
        """
        app.config.setdefault('PRETTIFY', False)

        if app.config['PRETTIFY']:
            app.after_request(self._prettify_response)

    def _prettify_response(self, response):
        """
        Prettify the HTML response.

        :param response: A Flask Response object.
        """
        if response.content_type == 'text/html; charset=utf-8':
            ugly = response.get_data(as_text=True)
            soup = BeautifulSoup(ugly, 'html.parser')
            pretty = soup.prettify(formatter='html')
            response.direct_passthrough = False
            response.set_data(pretty)

        return response
