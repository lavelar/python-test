import pytest
from principal import soma
from principal import multiplica


def test_soma():
    assert soma(2, 4)==6

def test_multiplica():
    assert multiplica(2, 5)==10