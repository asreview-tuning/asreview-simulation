import click

from .balancers import double_balancer
from .balancers import no_balancer
from .balancers import triple_balancer
from .balancers import undersample_balancer
from .classifiers import naive_bayes_classifier
from .classifiers import random_forest_classifier
from .classifiers import logistic_classifier
from .classifiers import lstm_base_classifier
from .classifiers import lstm_pool_classifier
from .classifiers import nn_2_layer_classifier
from .classifiers import svm_classifier
from .extractors import doc2vec_extractor
from .extractors import tfidf_extractor
from .extractors import embedding_idf_extractor
from .extractors import embedding_lstm_extractor
from .extractors import sbert_extractor
from .samplers import random_prior_sampler
from .samplers import handpicked_prior_sampler
from .queriers import cluster_querier
from .queriers import mixed_querier
from ._load_config import load_config
from ._print_settings import print_settings
from ._simulate import simulate
from ._state import State


cli_help = """
Example usage:\n
    $ asreview-cli print-settings\n
    $ asreview-cli simulate labeled-records.ris\n
Commands can be chained together, e.g.\n
    $ asreview-cli load-config thefile.cfg simulate labeled-records.ris\n
    $ asreview-cli load-config thefile.cfg simulate labeled-records.ris\n
    $ asreview-cli b-double --alpha 1.23 print-settings\n
"""


@click.group("cli", chain=True, help=cli_help)
@click.pass_context
def group(ctx):
    if ctx.obj is None:
        ctx.obj = State()


group.add_command(double_balancer)
group.add_command(no_balancer)
group.add_command(triple_balancer)
group.add_command(undersample_balancer)
group.add_command(naive_bayes_classifier)
group.add_command(random_forest_classifier)
group.add_command(logistic_classifier)
group.add_command(lstm_base_classifier)
group.add_command(lstm_pool_classifier)
group.add_command(nn_2_layer_classifier)
group.add_command(svm_classifier)
group.add_command(doc2vec_extractor)
group.add_command(tfidf_extractor)
group.add_command(embedding_idf_extractor)
group.add_command(embedding_lstm_extractor)
group.add_command(sbert_extractor)
group.add_command(random_prior_sampler)
group.add_command(handpicked_prior_sampler)
group.add_command(cluster_querier)
group.add_command(mixed_querier)
group.add_command(load_config)
group.add_command(print_settings)
group.add_command(simulate)