import click
@click.group()
def cli():
    pass
@cli.command()
def models():
    f = open('django/models.py','r')
    click.echo('  ')
    click.echo('Simple Example on how to write simple models in django .')
    click.echo('  ')
    click.echo(f.read())
    f.close()
@cli.command()
def urls():
    f = open('django/urls.py','r')
    click.echo(' ')
    click.echo('Simple Example on how to write django urls page .')
    click.echo('  ')
    click.echo(f.read())
    f.close()
@cli.command()
def forms():
    f = open('django/forms.py','r')
    click.echo('  ')
    click.echo('Simple Example on how to write forms in Django')
    click.echo(' ')
    click.echo(f.read())
    f.close()
@cli.command()
def views():
    f = open('django/views.py','r')
    click.echo(' ')
    click.echo('Simple Example of how to write Views in django .')
    click.echo(' ')
    click.echo(f.read())
    f.close()
