#!/usr/bin/env python
from setuptools import setup

version = '1.5.0'

setup(
    name='django-widgets-improved',
    version=version,
    author='Simon Hanna',
    author_email='simhnna@gmail.com',
    url='https://github.com/simhnna/django-widgets-improved',
    description='Tweak the form field rendering in templates, not in python-level form definitions.',
    long_description=open('README.md').read() + "\n\n" + open('CHANGELOG.md').read(),
    license='MIT license',
    requires=['django (>= 1.8)'],
    packages=['widget_tweaks', 'widget_tweaks.templatetags'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

