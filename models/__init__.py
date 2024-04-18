#!/usr/bin/python3
"""__init__magic method for models
    creates a unique FileStorage instance for the application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

