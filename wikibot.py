import click

from mylib.bot import scrape

@click.command()
@click.option(
    '--name',
    prompt='wikipedia page to scrape',
    help='web page we want to scrape'
    )


def cli(name):
    result=scrape(name)
    click.echo(result) 

if __name__=='__main__':
    cli()
