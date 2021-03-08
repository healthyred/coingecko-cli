from setuptools import setup

setup(
    name='CoinGeckoCLI',
    version='1.01',
    py_modules=['coingecko'],
    install_requires=[
        'Click',
        'Requests',
    ],
    entry_points='''
        [console_scripts]
        coingecko=coingecko:cli
    ''',
)