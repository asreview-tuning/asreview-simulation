import click
from asreview.models.query import UncertaintyQuery
from .._epilog import epilog


name = UncertaintyQuery.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Uncertainty query strategy",
    name=f"qry-{name}",
    short_help="Uncertainty query strategy",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--n_instances",
    "n_instances",
    default=1,
    help="Number of records per query",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def uncertainty_querier(obj, force, n_instances):
    if not force:
        assert obj.provided.querier is False, (
            "Attempted reassignment of querier. Use the --force flag "
            + "if you mean to overwrite the querier configuration from previous steps. "
        )
    obj.querier.abbr = name
    obj.querier.params = {
        "n_instances": n_instances,
    }
    obj.provided.querier = True
