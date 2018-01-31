import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand
from codecs import open


here = os.path.abspath(os.path.dirname(__file__))

modules = ['flask_pretty']

requires = [
    'beautifulsoup4',
    'flask',
]

tests_require = [
    'docutils',
    'tox'
]

about = {}
with open(os.path.join(here, '__about__.py'), mode='r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.rst', mode='r', encoding='utf-8') as f:
    readme = f.read()


class ToxTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    long_description=readme,
    py_modules=modules,
    install_requires=requires,
    tests_require=tests_require,
    cmdclass={'test': ToxTest},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
