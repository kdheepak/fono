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
            click.secho(help_str)
            click.get_current_context().exit()

        if kwargs['folder']:
            price, quantity, shipping = data.get_input(kwargs['folder'])
        elif kwargs['quantity'] and kwargs['price'] and kwargs['shipping']:
            quantity = data.get_quantity(kwargs['quantity'])
            price = data.get_price(kwargs['price'])
            shipping = data.get_shipping(kwargs['shipping'])

        model = ReferenceModel.create_model(price, quantity, shipping)

        click.secho("Solving...", fg='blue', bold=True)

        # solve.display_results(solve.solve_instance(model), model)
        solve.solve_instance(model), model

        click.echo("")

        click.secho("fono results:", fg='green', bold=True)

        click.echo("")

        for website in sorted(model.Websites):
            for item in sorted(model.Items):
                if model.Quantity[website, item].value>0:
                    click.echo("Buy ", nl=False)
                    click.secho("{} ".format(model.Quantity[website, item].value), bold=True, nl=False)
                    click.echo("item(s) of ", nl=False)
                    click.secho("{} ".format(item), bold=True, nl=False)
                    click.echo("from ", nl=False)
                    click.secho("{}.".format(website), bold=True)

        click.echo("")

        item_costs = model.Cost['Item'].value
        shipping_costs = model.Cost['Shipping'].value
        total_costs = item_costs + shipping_costs

        click.secho("Total product costs = {}".format(item_costs), bold=True)
        click.secho("Total shipping costs = {}".format(shipping_costs), bold=True)
        click.secho("Total costs = {}".format(total_costs), fg='green', bold=True)

    except Exception as e:
        click.echo('')
        raise click.ClickException("{}\n\nCheck the help (--help) on how to use fono or contact the developer.".format(e.message))

if __name__ == '__main__':
    main()
