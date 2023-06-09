import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_with_records():
    runner = CliRunner()
    args = [
        "sam-handpicked",
        "--records",
        "1,2,3",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    sampler = json.loads(result.output)["sampler"]
    assert sampler["abbr"] == "handpicked"
    params = sampler["params"].keys()
    assert len(params) == 1
    assert "records" in params
    assert "rows" not in params
    assert sampler["params"]["records"] == [1, 2, 3]


def test_with_rows():
    runner = CliRunner()
    args = [
        "sam-handpicked",
        "--rows",
        "1,2,3",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    sampler = json.loads(result.output)["sampler"]
    assert sampler["abbr"] == "handpicked"
    params = sampler["params"].keys()
    assert len(params) == 1
    assert "records" not in params
    assert "rows" in params
    assert sampler["params"]["rows"] == [1, 2, 3]
