from setuptools import setup, find_packages

setup(
    name='TuModeloDeClientes+Fernandez',
    version='0.1.0',
    description='Un modelo de clientes para una tienda online',
    author='Luis Fernandez',
    author_email='luis.fernandeez@google.com',
    packages=find_packages(),  # Encuentra automáticamente los paquetes
    install_requires=[],  # Lista de dependencias
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)