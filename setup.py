from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='alissimplemath',
    version='0.0.2',
    author='Alisson Guarniêr',
    author_email="alisson.dfla@hotmail.com",
    description='Um pacote simples de operações matemáticas para fins de aprendizado',
    long_description=readme,
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