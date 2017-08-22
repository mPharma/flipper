"""
Feature flipper that uses environment variables to ftoggle features
"""
import os


def empty_func():
    pass

def flippit(feature_name, newFunc=None, oldFunc=None):
    if 1 == int(os.getenv('FEATURE_{}'.format(feature_name.upper()), 0)):
        return newFunc if newFunc is not None else empty_func
    else:
        return oldFunc if oldFunc is not None else empty_func