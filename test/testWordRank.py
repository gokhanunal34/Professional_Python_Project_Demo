"""
Some basic tests
"""

import pkgutil

from src.wordRank import WordRank
from src.wordRank.errors import NotReadyException

# Immediately parse with wrObject1 and leave wrObject2 fallow.
wrObject1 = WordRank("../input/MobyDick_Chapter1.txt")
# rawdata = pkgutil.get_data(__package__, "input/MobyDick_Chapter1.txt")
wrObject2 = WordRank()


# Verify that bool values returned when no words processed is False, and vice versa.
def test_wordrank_bool():
    assert bool(wrObject1) is True and bool(wrObject2) is not True


# Verify that if a word isn't in the count dictionary then it returns 0 as its count.
def test_wordrank_values():
    assert wrObject1.get_total_words() == 2193
    assert wrObject2.get_total_words() == 0
    assert wrObject1["particular"] == 2
    assert wrObject2["particular"] == 0
    assert wrObject1[0] == []
    assert wrObject2[0] == []


# Verify that the NotReadyException is raised when an attempt is made to parse on a
# WordRank object that isn't ready to parse.
def test_wordrank_already_parsed():
    try:
        wrObject1.parse("../input/MobyDick_Chapter1.txt", True)
    except NotReadyException:
        assert True
        return

    assert False


# Tests reset, stopword, and getitem functionality.
def test_wordrank_include_stopwords():
    wrObject1.reset()
    wrObject2.reset()
    wrObject1.parse(file_name="../input/MobyDick_Chapter1.txt", exclude_stopwords=False)
    wrObject2.parse(file_name="../input/MobyDick_Chapter1.txt", exclude_stopwords=True)
    assert wrObject1["the"] == 124
    assert wrObject2["the"] == 0
    assert wrObject1[10] == ["or", "sea", "his", "one"]
    assert wrObject2[10] == ["sea", "his", "one"]
    assert wrObject1[124] == ["the"]
    assert wrObject2[124] == []


# Tests that ranking is as expected.
def test_wordrank_most_counted():
    iterator1 = iter(wrObject1.get_rankings())
    iterator2 = iter(wrObject2.get_rankings())

    assert next(iterator1)[1] == "the"
    assert next(iterator1)[1] == "of"
    assert next(iterator1)[1] == "and"

    assert next(iterator2)[1] == "i"
    assert next(iterator2)[1] == "me"
    assert next(iterator2)[1] == "you"


# test iteration a bit.
def test_wordrank_iterator():
    iterator1 = iter(wrObject1)
    iterator2 = iter(wrObject2)

    next(iterator1) == "chapter"
    next(iterator2) == "chapter"


def test_get_datastructures():
    word_counts = wrObject2.get_word_counts()
    stopword_counts = wrObject2.get_stopword_counts()

    assert word_counts["i"] == wrObject2["i"]
    assert stopword_counts["a"] == wrObject2._stopword_count["a"]
