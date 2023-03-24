from ._base_extractor import BaseExtractor
from ._doc2vec_extractor import Doc2VecExtractor
from ._embedding_idf_extractor import EmbeddingIdfExtractor
from ._embedding_lstm_extractor import EmbeddingLstmExtractor
from ._sbert_extractor import SbertExtractor
from ._tfidf_extractor import TfidfExtractor


def list_extractors():
    extractors = [
        Doc2VecExtractor,
        EmbeddingIdfExtractor,
        EmbeddingLstmExtractor,
        SbertExtractor,
        TfidfExtractor
    ]
    return {e.name: e for e in extractors}


del _base_extractor
del _doc2vec_extractor
del _embedding_idf_extractor
del _embedding_lstm_extractor
del _sbert_extractor
del _tfidf_extractor
