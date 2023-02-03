"""
examples of using pathlib and os
"""

import pathlib


my_path = pathlib.Path(".")
print('\nThis is my current working path:')
print(my_path.cwd())

print("\nIf main.py exists:")
print(pathlib.Path('main.py').exists())

print("\nIf phone.py exists:")
print(pathlib.Path('phone.py').exists())
