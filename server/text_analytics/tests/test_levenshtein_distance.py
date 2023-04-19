import pytest
from server.text_analytics.levenshtein_distance import calculate_levenshtein_distance

def test_calculate_edit_distance():
    ''' Test simple Levenshtein calc one character mistyped'''

    lev_distance = calculate_levenshtein_distance({
        "s1": "test1",
        "s2": "test12",
        "transpositions": False,
        "substitution_cost": 1
    })

    assert lev_distance == 1
