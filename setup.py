from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1.0',
    description='A test description',
    long_description='I would greet peope',
    author='Daksh Jain',
    author_email='daksh.jain00@gmail.com',
    url='https://github.com/Dakshjain1/internship-python-module',
    packages=find_packages(exclude=['*tests*']),
)