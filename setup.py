import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from codecs import open


here = os.path.abspath(os.path.dirname(__file__))

packages = find_packages()

requires = [
    'beautifulsoup4',
    'flask',
]

tests_require = [
    'docutils',
    'tox'
]

about = {}
with open(os.path.join(here, 'flask_pretty', '__about__.py'), mode='r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.rst', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    long_description=readme,
    packages=packages,
    install_requires=requires,
    tests_require=tests_require,
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
