import pytest

from utils import dicts

@pytest.fixture
def coll():
    return {1: '1', 2: '2', 3: True, 4: 4, 5: [1, 2]}

def test_get_default(coll):
    assert dicts.get_val(coll, 6) == 'git'

def test_get_correct_value(coll):
    assert dicts.get_val(coll, 1) == '1'

def test_get_from_empty_dict():
    assert dicts.get_val({}, 1, 'empty') == 'empty'
