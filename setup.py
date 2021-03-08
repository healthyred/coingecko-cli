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

# setup(
#     name='HelloWorld',
#     version='1.0',
#     py_modules=['hello'],
#     install_requires=[
#         'Click',
#     ],
#     entry_points='''
#         [console_scripts]
#         hello=hello:cli
#     ''',
# )