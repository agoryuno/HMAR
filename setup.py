from setuptools import setup, find_packages

print (find_packages())

setup(
    name='HMAR',
    version='0.0.1',
    author='Alex Goryunov',
    author_email='alex.goryunov@gmail.com',
    description='Simplified code for the HMAR model',
    long_description='Original T3PR and HMAR models are at: https://github.com/brjathu/T3DP',
    url='https://github.com/agoryuno/HMAR',
    packages=find_packages(),
    install_requires=[
        "torch",
        "numpy",
        "yacs"
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
