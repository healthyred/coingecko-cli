import click
import json
import requests
import click

# def get_price():
#     resp = requests.get(
#         'https://api.coingecko.com/api/v3/simple/price',
#         params={'ids': 'ethereum', 'vs_currencies': 'usd'}
#     )
#     return resp.json()['ethereum']['usd']

@click.command()
def cli():
    click.echo("Hello World!")
