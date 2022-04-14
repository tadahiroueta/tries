from setuptools import find_packages, setup

setup(
  name='tries',
  version='1.0.0',
  packages=find_packages(),
  install_requires=[
    'click',
    'mysql-connector'
  ],
  entry_points='''
  [console_scripts]
  tries=tries:tries
  '''
)