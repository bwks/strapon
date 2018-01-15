import os
from setuptools import setup


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as f:
        return f.read()

setup(
    name='strapon',
    version='0.1',
    author='Brad Searle',
    author_email='bradleysearle@gmail.com',
    packages=['strapon',
              'tests'],
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    long_description=read('README.md'),
    install_requires=[''],
)