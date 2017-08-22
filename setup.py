from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='flipper',
    version='0.0.1',
    author='James Finucane',
    author_email='james@mpharma.co',
    packages=find_packages(exclude=['docs', 'tests', 'venv']),
    url='https://github.com/mPharma/flipper',
    license='MIT',
    description='Feature flipper that uses environment variables to ftoggle features',
    long_description=long_description,
    install_requires=[
    ]
)
