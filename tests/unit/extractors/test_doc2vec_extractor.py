import json
from click.testing import CliRunner
from asreview_simulation.cli import cli


def test_doc2vec_extractor_default_parameterization():
    runner = CliRunner()
    args = [
        "fex-doc2vec",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    extractor = json.loads(result.output)["extractor"]
    assert extractor["abbr"] == "doc2vec"
    params = extractor["params"].keys()
    assert "dbow_words" in params
    assert extractor["params"]["dbow_words"] == 0
    assert "dm" in params
    assert extractor["params"]["dm"] == 2
    assert "dm_concat" in params
    assert extractor["params"]["dm_concat"] == 0
    assert "epochs" in params
    assert extractor["params"]["epochs"] == 33
    assert "min_count" in params
    assert extractor["params"]["min_count"] == 1
    assert "n_jobs" in params
    assert extractor["params"]["n_jobs"] == 1
    assert "vector_size" in params
    assert extractor["params"]["vector_size"] == 40
    assert "window" in params
    assert extractor["params"]["window"] == 7
