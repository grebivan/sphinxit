from setuptools import setup, find_packages


setup(
    name='sphinxit',
    version='0.3.3',
    author='Grebivan (original Roman Semirook)',
    author_email='iv.grebenschikov@gmail.com',
    packages=find_packages(),
    license='BSD',
    url='https://github.com/grebivan/sphinxit',
    description='Lite and powerful SphinxQL query constructor',
    long_description='''Lite and powerful SphinxQL query constructor.
    This is a fork of https://github.com/semirook/sphinxit supporting Python3.''',
    install_requires=[
        "six>=1.1.0",
        "pymysql>=0.10.1,<0.11",
        "ordereddict>=1.1",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
