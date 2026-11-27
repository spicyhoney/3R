"""CLI script for the my_backend package. This will be called on the command line"""

import click

from my_backend.process import celsius_to_fahrenheit, hello_world


@click.command()
@click.option("--message", help="Type a message to say")
@click.option("--celsius", type=float, help="Convert Celsius to Fahrenheit.")
@click.version_option()
def my_backend_cli(message, celsius):
    """Print a message or convert a temperature."""
    if celsius is not None:
        if message is not None:
            raise click.UsageError("Choose either --message or --celsius.")
        fahrenheit = celsius_to_fahrenheit(celsius)
        click.echo(f"{celsius:g} °C = {fahrenheit:g} °F")
        return

    if message is None:
        message = click.prompt("message")
    click.echo(hello_world(message))
