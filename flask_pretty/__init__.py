from bs4 import BeautifulSoup

from .__about__ import (__title__, __version__, __description__, __author__,
                        __author_email__, __url__, __license__)


class Prettify(object):
    def __init__(self, app=None, **kwargs):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('PRETTIFY_PAGE', False)

        if app.config['PRETTIFY_PAGE']:
            app.after_request(self.prettify_response)

    def prettify_response(self, response):
        """
        Prettify HTML response for a better development experience
        """
        if response.content_type == u'text/html; charset=utf-8':
            ugly = response.get_data(as_text=True)
            soup = BeautifulSoup(ugly, "html.parser")
            pretty = soup.prettify(formatter='html')
            response.direct_passthrough = False
            response.set_data(pretty)

        return response
