#!/usr/bin/env python

from setuptools import setup, find_packages
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

		
setup(name='zutils_binder_test',
      version='1.0.0',
      description='misc utilities',
      author='Andrew Zulberti',
      author_email='andrew.zulberti@gmail.com',
      #packages=['zutils'],
      packages=find_packages(),
      install_requires=['numpy','matplotlib', 'zutils'],
      dependency_links=['https://github.com/iosonobert/zutils/tarball/master#egg=package-1.0'],
      license='unlicensed to all but author',
      include_package_data=True,
      distclass=BinaryDistribution,
    )
