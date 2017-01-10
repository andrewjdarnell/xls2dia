# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='xls2dia',
    version='0.1.0',
    description='xls2dia - Generate a diagram from a simple description in a spreadsheet or csv file',
    long_description=readme,
    author='Andrew Darnell',
    author_email='andrewjdarnell@gmail.com',
    url='https://github.com/andrewjdarnell/xls2dia',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

