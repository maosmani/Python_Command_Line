import click

@click.command()
@click.option('--models',is_flag=True,help="Show model example")
@click.option('--views' ,is_flag=True, help="show  views example")
@click.Option('--urls',is_flag=True,help='show how to code urls page')
@click.Option('--forms',is_flag=True,help='show forms example ')
def cli(models,views,urls,forms):
    if models:
        f = open('django/models.py','r')
        click.echo("model example .")
        click.echo(f.read())
        f.close()
    elif views:
        f = open('django/views.py','r')
        click.echo('views example ')
        click.echo(f.read())
        f.close()
    elif urls:
        f = open('django/urls.py','r')
        click.echo('urls examplae')
        click.echo(f.read())
        f.close()
    '''
    elif forms:
        f = open('django/forms.py','r')
        click.echo('form example')
        click.echo(f.read())
        f.close()
        '''
