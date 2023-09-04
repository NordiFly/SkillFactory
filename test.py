import os
from pathlib import Path

a = os.path.abspath(os.getcwd())
BASE_DIR = Path(__file__).resolve()

print(a)