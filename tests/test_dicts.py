from utils import dicts

def test_get_default():
    assert dicts.get_val({1: '1', 2: '2', 3: True, 4: 4, 5: [1, 2]}, 6) == 'git'

def test_get_correct_value():
    assert dicts.get_val({1: '1', 2: '2', 3: True, 4: 4, 5: [1, 2]}, 1) == '1'

def test_get_from_empty_dict():
    assert dicts.get_val({}, 1, 'empty') == 'empty'
