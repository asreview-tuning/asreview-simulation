import click


@click.command("simulate", help="Run simulation and exit; terminates parsing\n\n    DATA_FILE: " +
               "path to the fully labeled data")
@click.argument("data_file", type=click.Path(exists=True, readable=True))
@click.option("--write-interval", "write_interval", type=click.INT, help="Write interval.")
@click.pass_obj
def simulate(obj, data_file, write_interval):
    click.echo("simulation starting")
    click.echo("doing things...")
    click.echo("simulation ended")