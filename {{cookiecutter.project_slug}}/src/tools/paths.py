import os
from pathlib import Path

EXPERIMENT_ROOT = Path(os.getenv('EXPERIMENT_ROOT'))

def set_cwd(path):
    os.chdir(path)
