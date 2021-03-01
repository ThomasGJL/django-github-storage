 #!/usr/bin/env python3
 # -*- coding: utf-8 -*- 
from setuptools import setup, find_packages

setup(name='django-github-storage',
      version='1.0.0',
      description="Use github as storage",
      packages=find_packages(),
      keywords='github, storage',
      author='ThomasIBM',
      author_email='guojial@cn.ibm.com',
      license="Apache License, Version 2.0",
      url='https://github.com/ThomasIBM/django-github-storage',
      include_package_data=True,
      zip_safe=False,
)