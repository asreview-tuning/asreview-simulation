import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_max_uncertainty_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qry-max-uncertainty",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["abbr"] == "max_uncertainty"
    params = querier["params"].keys()
    assert len(params) == 2
    assert "mix_ratio" in params
    assert querier["params"]["mix_ratio"] == 0.95
    assert "n_instances" in params
    assert querier["params"]["n_instances"] == 1
