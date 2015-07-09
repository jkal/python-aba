from distutils.core import setup

setup(
    name='aba',
    author='John Kalantzis',
    author_email='john@jkal.net',
    version='0.2',
    packages=[
        'aba',
    ],
    url='https://github.com/jkal/python-aba',
    license='MIT License',
    description='Python library to generate ABA (Cemtext) files.',
    long_description=open('README.rst').read()
)
