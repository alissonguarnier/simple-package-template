from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='mathsimple',
    version='0.0.1',
    author='Alisson Guarniêr',
    author_email="alisson.dfla@hotmail.com",
    description='Um pacote simples de operações matemáticas para fins de aprendizado',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/alissonguarnier/simple-package-template.git",
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=requirements,
    python_requires='>=3.6',
)