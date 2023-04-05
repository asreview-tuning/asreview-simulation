from ._base import BaseDataset
from ._first_dataset import FirstDataset
from ._second_dataset import SecondDataset


del _base
del _first_dataset
del _second_dataset

__all__ = [
    "BaseDataset",
    "FirstDataset",
    "SecondDataset"
]

for _item in dir():
    if not _item.endswith('__'):
        assert _item in __all__, f"Named export {_item} missing from __all__ in {__package__}"
for _item in __all__:
    assert _item in dir(), f"__all__ includes unknown item {_item} in {__package__}"
del _item
