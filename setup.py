"""Handles packaging, distribution, and testing."""


import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
from setuptools import find_packages


setup(

	# Basic package information.
	name = 'pycall',
	version = '2.0',
	packages = find_packages(),

	# Packaging options.
	zip_safe = False,
	include_package_data = True,

	# Package dependencies.
	install_requires = 'docutils>=0.7',
	tests_require = ['coverage>=3.4', 'nose>=0.11.4'],

	# Metadata for PyPI.
	author = 'Randall Degges',
	author_email = 'rdegges@gmail.com',
	license = 'UNLICENSE',
	url = 'http://pycall.owlyy.org/',
	keywords = 'asterisk callfile call file telephony voip',
	description = 'A flexible python library for creating and using Asterisk' \
			' call files.',
	long_description = open('README').read()

)
