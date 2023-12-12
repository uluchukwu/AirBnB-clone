#!/usr/bin/python3
"""__init__magic method for models
    creats a unique Filestorage instance for the application"""
    from models.engine.file_storage import Filestorage
    

    storage = Filestorage()
    storage.relload()
