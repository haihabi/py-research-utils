
from imp import find_module

def is_package_installed(mod):
    try:
        op = find_module(mod)
        return True
    except ImportError:
        return False