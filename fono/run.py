#!/usr/bin/env python

import click

import solve
import data
import ReferenceModel
import version

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('--folder', type=click.Path(), help='Path to data folder')
@click.option('--quantity', type=click.Path(), help='Path to quantity.csv file')
@click.option('--price', type=click.Path(), help='Path to price.csv file')
@click.option('--shipping', type=click.Path(), help='Path to shipping.csv file')
@click.version_option(version.__version__, '-v', '--version')
def main(**kwargs):
    """
    'Find Optimal Number of Orders' aka fono
    """

    try:

        if kwargs['folder'] is None and kwargs['quantity'] is None and kwargs['price'] is None and kwargs['shipping'] is None:
            help_str = "{}".format(click.get_current_context().get_help())
            click.secho(help_str, color='green')
            click.get_current_context().exit()

        if kwargs['folder']:
            price, quantity, shipping = data.get_input(kwargs['folder'])
        elif kwargs['quantity'] and kwargs['price'] and kwargs['shipping']:
            quantity = data.get_quantity(kwargs['quantity'])
            price = data.get_price(kwargs['price'])
            shipping = data.get_shipping(kwargs['shipping'])

        model = ReferenceModel.create_model(price, quantity, shipping)

        solve.display(solve.solve_instance(model))

    except Exception as e:
        click.echo('')
        raise click.ClickException("{}\n\nCheck the help (--help) on how to use fono or contact the developer.".format(e.message))

if __name__ == '__main__':
    main()
