from setuptools import setup, find_packages

setup(
    name='package_name',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Zipho-Matiso/package_name',
    author='Zipho',
    author_email='zipohmts@gmail.com'
    )
