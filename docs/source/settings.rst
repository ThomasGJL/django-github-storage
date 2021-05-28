========
Settings
========

This document describes the Django settings that can be used to customize the configuration
of ``django-github-storage``.

.. py:attribute:: DEFAULT_FILE_STORAGE

   :default: ``django.core.files.storage.FileSystemStorage``

   ``django_github_storage.storage.FileSystemStorage``

.. py:attribute:: GIT_TOKEN

   :default: No default

   Get the token from your github server.

.. py:attribute:: GIT_URL

   :default: No default

   Get the url from your github server.

.. py:attribute:: MEDIA_FOLDER_NAME

   :default: No default

   The folder name need copy back to your django/wagtail folder.
