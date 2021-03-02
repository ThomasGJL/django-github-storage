 #!/usr/bin/env python3
 # -*- coding: utf-8 -*- 
from setuptools import setup, find_packages

setup(name='django-github-storage',
      version='1.0.2',
      description="Use github as storage",
      packages=find_packages(),
      keywords='github, storage',
      author='Thomas',
      author_email='thomasguo1127@gmail.com',
      license="Apache License, Version 2.0",
      url='https://github.com/ThomasGJL/django-github-storage',
      include_package_data=True,
      zip_safe=False,
)