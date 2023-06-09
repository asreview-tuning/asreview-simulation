import click
from asreview.models.query import MaxRandomQuery
from .._epilog import epilog


name = MaxRandomQuery.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use a Mixed query strategy (Max and Random)",
    name=f"qry-{name}".replace("_", "-"),
    short_help="Mixed query strategy (Max and Random)",
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
    "--mix_ratio",
    "mix_ratio",
    default=0.95,
    help="Mix ratio",
    show_default=True,
    type=click.FLOAT,
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
def max_random_querier(obj, force, mix_ratio, n_instances):
    if not force:
        assert obj.provided.querier is False, (
            "Attempted reassignment of querier. Use the --force flag "
            + "if you mean to overwrite the querier configuration from previous steps. "
        )
    obj.querier.abbr = name
    obj.querier.params = {
        "mix_ratio": mix_ratio,
        "n_instances": n_instances,
    }
    obj.provided.querier = True
