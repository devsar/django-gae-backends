#!/usr/bin/env python

from distutils.core import setup

setup(name='django-gae-backends',
      version='0.1',
      description='Django Backends for the Google App Engine',
      author='Sebastian Serrano',
      author_email='sebastian@devsar.com',
      url='https://github.com/devsar/django-gae-backends',
      packages=['gae_backends', 'gae_backends.sessions'],
     )

