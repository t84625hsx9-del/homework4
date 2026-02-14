from . import models
from . import jsonplaceholder_requests
from . import main

# Определяем, какие имена будут импортироваться при использовании 'from homework_04 import *'
__all__ = [
    "models",
    "jsonplaceholder_requests",
    "main",
]
