import click
import json
import requests
import click

## TODO: move to separate APIutils
def get_price(coinName, vsCurrency, debug):
    resp = requests.get(
        'https://api.coingecko.com/api/v3/simple/price',
        params={'ids': coinName, 'vs_currencies': vsCurrency}
    )

    if debug:
        print(resp.json())

    return resp.json()[coinName.lower()][vsCurrency.lower()]

def get_coin_list():
    resp = requests.get(
        'https://api.coingecko.com/api/v3/coins/list',
    )
    return resp.json()

class Context(object):

    def __init__(self, debug=False):
        self.debug = debug

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))
    ctx.obj = Context(debug)

@cli.command()
@click.argument('coin-name')
@click.option('--vs-currency', default='usd',
              help='This is the currency we will show value in.')
@click.pass_context
def coin(ctx, coin_name, vs_currency):
    """
    Command to find the value of a coin in any currency. The default is USD.

    :param coin_name: Id of the coin to query
    :param vs_currency: Currency to display value in
    :return:
    """
    click.echo('%s is priced at %s in %s' % (coin_name, get_price(coin_name, vs_currency, ctx.obj.debug), vs_currency))

@cli.command()
def get_coinList():
    toPrint = ""
    coinList = get_coin_list()

    for coinData in coinList:
        toPrint += (" Name: " + coinData['name'] + " Id: " + coinData['id'] + "\n")
    click.echo(toPrint)
