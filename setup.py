#!/usr/bin/env python

from setuptools import setup, find_packages
import os
setup(name='smalltalk',
      version='0.0.1',
      description='Talk to gl-js maps through terminal',
      author='Bennett Murphy',
      author_email='murphy214@live.marshall.edu',
      url='https://github.com/murphy214/smalltalk',
      packages=['smalltalk'],
      #dependency_links=['http://github.com/murphy214/nlgeojson/tarball/master#egg=package-1.0'],#http://github.com/murphy214/pipeleaflet/tarball/master#egg=package-1.1','http://github.com/murphy214/pipevts/tarball/master#egg=package-1.0','http://github.com/murphy214/pipegls/tarball/master#egg=package-1.0']

      dependency_links = ['http://github.com/murphy214/nlgeojson/tarball/master#egg=nlgeojson-1.0.0']

      #dependency_links=['http://github.com/murphy214/nlgeojson.git#egg=nlgeojson-1.0']#http://github.com/murphy214/pipeleaflet/tarball/master#egg=package-1.1','http://github.com/murphy214/pipevts/tarball/master#egg=package-1.0','http://github.com/murphy214/pipegls/tarball/master#egg=package-1.0']

      )

# delete this better for use locally
#os.system('pip install -r requirements.txt')
