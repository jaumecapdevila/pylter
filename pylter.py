import sys
import click

def strip_list(elements):
    return map(str.strip, elements)

def make_unique(elements):
    return set(elements)

@click.command()
@click.option('--output', default='\n', help='Specify the element to join the resulting list.')
def main(output):
    unique = make_unique(strip_list(sys.stdin))
    click.echo(output.join(unique))

if __name__ == "__main__":
    main()
