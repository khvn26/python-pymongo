#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='PyMongo-OpenTracing',
    version='0.0.1',
    url='http://github.com/signalfx/python-mongo',
    download_url='http://github.com/signalfx/python-mongo/tarball',
    author='SignalFx, Inc.',
    author_email='info@signalfx.com',
    description='OpenTracing support for PyMongo',
    packages=find_packages(),
    platforms='any',
    license='Apache Software License v2',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'License :: OSI Approved :: Apache Software License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'opentracing>=2.0,<2.1',
        'pymongo>=3.1'
    ],
    extras_require={
        'tests': [
            'docker',
            'mock',
            'pytest'
        ],
    },
)
