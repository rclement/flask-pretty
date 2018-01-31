import os
import unittest

from flask import Flask, render_template
from flask.json import jsonify
from flask_pretty import Prettify


current_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(current_dir, 'templates')
with open(os.path.join(templates_path, 'pretty.html'),
          mode='r', encoding='utf-8') as f:
    pretty_template = f.read()
    pretty_template = pretty_template.encode('utf-8')


class TestPretty(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__, template_folder=templates_path)
        app.testing = True
        app.config['PRETTIFY'] = True
        self.app = app
        self.prettify = Prettify(app)

        @app.route('/ugly')
        def ugly():
            return render_template('ugly.html')

        @app.route('/pretty')
        def pretty():
            return render_template('pretty.html')

        @app.route('/json')
        def json():
            return jsonify({
                'data': []
            })

    def test_ugly_html_template(self):
        rv = self.app.test_client().get('/ugly')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.mimetype, 'text/html')
        self.assertEqual(pretty_template, rv.data)

    def test_pretty_html_template(self):
        rv = self.app.test_client().get('/pretty')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.mimetype, 'text/html')
        self.assertEqual(pretty_template, rv.data)

    def test_non_html_template(self):
        rv = self.app.test_client().get('/json')
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.mimetype, 'application/json')


if __name__ == '__main__':
    unittest.main()
