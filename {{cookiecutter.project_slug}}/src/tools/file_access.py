import os
from pathlib import Path

EXPERIMENT_ROOT = os.getenv('EXPERIMENT_ROOT')

def get_file(file):
    return Path(file).resolve()

def get_data_file(kind, file):
    return Path(EXPERIMENT_ROOT, 'data', kind, file)

def get_bin_file(file):
    return Path(EXPERIMENT_ROOT, 'bin', file)
