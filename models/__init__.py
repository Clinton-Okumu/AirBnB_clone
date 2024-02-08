#!/usr/bin/python3
"""__init__magic method for the directories"""
from models.engine.file_storage import fileStorage

store = fileStorage()
store.reload()
