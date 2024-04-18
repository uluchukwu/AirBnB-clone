#!/usr/bin/python3
<<<<<<< HEAD
"""__init__magic method for models
    creates a unique FileStorage instance for the application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

=======
"""Initializes the package"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
>>>>>>> 962328f7111c914960802a02e740070343dff5dd
