#!/usr/bin/env python

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

VERSION='0.1.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
	long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
	requirements = f.readlines()

setup(name='pubrunner',
	version=VERSION,
	description='A framework to rerun text mining tools on the latest publications',
	long_description=long_description,
	classifiers=[
		'Intended Audience :: Developers',
		'Intended Audience :: Education',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Science/Research',
		'License :: OSI Approved :: MIT License',
		'Operating System :: Unix',
		'Operating System :: MacOS :: MacOS X',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.6',
		'Topic :: Scientific/Engineering',
	],
	url='http://github.com/jakelever/kindred',
	author='Jake Lever',
	author_email='jake.lever@gmail.com',
	license='MIT',
	packages=['pubrunner'],
	install_requires=requirements,
	include_package_data=True,
	entry_points = {
        'console_scripts': ['pubrunner=pubrunner.command_line:main'],
    },
	zip_safe=False,
	test_suite='nose.collector',
	tests_require=['nose'])
