from setuptools import setup


setup(name='hello',
      packages=['hello'],
      entry_points={'console_scripts': ['hello=hello:cli']})
