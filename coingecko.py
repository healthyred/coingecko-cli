import click
import json
import requests
import click

def get_price(coinName, vsCurrency):
    resp = requests.get(
        'https://api.coingecko.com/api/v3/simple/price',
        params={'ids': coinName, 'vs_currencies': vsCurrency}
    )
    return resp.json()['ethereum']['usd']

@click.command()
@click.option('--coin-name', default='ethereum',
              help='This is the cryptocurrency we will query for.')
@click.option('--vs-currency', default='usd',
              help='This is the currency we will show value in.')
def cli(coin_name, vs_currency):
    click.echo(get_price(coinName, vsCurrency))

