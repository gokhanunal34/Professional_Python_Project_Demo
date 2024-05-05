"""
Author: Gokhan Unal
File: wordRank.py
Date: Spring 2024
Course: CIS4930 - Python
Institution: Florida State University

Reads a file and counts the instances of words.
"""

import string
from collections import defaultdict
from string import punctuation
from wordRank.errors import NotReadyException
from wordRank.util.filter import STOPWORDS


class WordRank:
    """
    A class that counts the occurrences of words in a utf8 text file.
    """

    def __init__(self, file_name: str = None, exclude_stopwords=True):
        self._input_file = file_name
        self._exclude_stopwords = exclude_stopwords
        self._word_count = {}
        self._stopword_count = {}
        self._word_ranks = defaultdict(list)
        self._num_words = 0
        if file_name:
            self.parse(file_name, self._exclude_stopwords)

    def parse(self, file_name, exclude_stopwords=True) -> None:
        """
        A method that accepts a filename and attempts to count all words from the
        provided file.

        If self._num_words is greater than 0 (parsing has already been done) then
        a NotReadyException should be raised to let the user know to reset the
        WordRank object before attempting to parse.

        Next, the self._exclude_stopwords variable should be set according to the
        user input with a default value of True if the user didn't specify.

        Third attempt to open a file and parse it, similarly to the way it was
        done in the previous assignment. Encoding for the call to 'open' should
        be utf-8.

        While parsing, if _store_word returns True increment self._num_words.

        Finally, call self._make_word_ranks() to build a dictionary mapping
        from count to a list of words that had that number of occurrences in
        the file (if 'i', 'me', and 'you' were the words that were counted 2
        times then the list for the index 2 would be those 3 words.).

        Parameters
        ==========
        :file_name: The name of the file to process
        :file_name type: string
        :exclude_stopwords: if true then don't include stopwords in main count.
        :exclude_stopwords type: boolean

        Raises
        ======
        :NotReadyException: An exception that specifies the wordrank object
            is already in a state of having processed a file, and needs to
            be reset.
        :FileNotFoundError: An exception that specifies the wordrank object
            could not access the file specified in file_name.
        :UnicodeDecodeError: An exception that specifies the wordrank object
            could not decode a file as utf-8.
        """
        if self._num_words > 0:
            raise NotReadyException("***Error with WordRank object")
        self._exclude_stopwords = exclude_stopwords
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                for word in line.split():
                    transformed_word = self._transform_word(word)
                    if self._store_word(transformed_word):
                        self._num_words += 1
        self._make_word_ranks()

    def _transform_word(self, token) -> str:
        """
        Remove leading and trailing whitespace from the token, then transform
        it to all lowercase.

        If the token ends with the substring "'s" then remove those last two
        characters from the token.

        Finally, remove all punctuation occurrences (as defined by
        string.punctuation) from the token, and then return the transformed
        token.
        """
        token: str = token.strip().lower()
        if token.endswith("'s"):
            token = token[:-2]
        return token.translate(str.maketrans("", "", string.punctuation))

    def _store_word(self, token) -> bool:
        """
        If the token is None or an empty string then immediately return False.

        If self._exclude_stopwords is True and the token is in STOPWORDS then
        increment the count for the token in self._stopword_count.

        Otherwise increment the count for the token in self._word_count.

        At the end of the method return True.
        """
        # check if token is none. It is done by NOT identifier
        if token is None or token == "":
            return False
        if self._exclude_stopwords and token in STOPWORDS:
            self._stopword_count[token] = self._stopword_count.get(token, 0) + 1
        else:
            self._word_count[token] = self._word_count.get(token, 0) + 1
        return True

    def _make_word_ranks(self):
        """
        Cycle through self._word_count, creating lists of words that
        correspond to a count. An inverted representation of self._word_count.
        """
        for word, count in self._word_count.items():
            if count not in self._word_ranks:
                self._word_ranks[count] = []
            self._word_ranks[count].append(word)

    def reset(self) -> None:
        """
        Readies the object to process another file by resetting class variables.
        """
        self._word_count = {}
        self._stopword_count = {}
        self._word_ranks = defaultdict(list)
        self._num_words = 0

    def get_total_words(self) -> int:
        """
        Returns the total number of words processed during the last parse.
        """
        return self._num_words

    def get_word_counts(self) -> dict:
        """
        Returns a reference to self._word_count.
        """
        return self._word_count

    def get_stopword_counts(self) -> dict:
        """
        Returns a reference to self._stopword_count.
        """
        return self._stopword_count

    def get_rankings(self) -> iter:
        """
        Returns an iterator that can be used to retrieve the word rankings
        from most counted to least counted.

        Populate a list with tuples of (count, word), sort the list and
        reverse it.

        Once you have the sorted and reversed list return an interator to
        it.
        """
        # comprehension baby!
        ranking_dict = [(count, word) for word, count in self._word_count.items()]
        ranking_dict.sort(reverse=True)
        return iter(ranking_dict)

    def __bool__(self):
        """
        Return True if self._num_words is greater than 0 (a valid file
        has been parsed).
        Otherwise return False.
        """
        return self._num_words > 0

    def __getitem__(self, i):
        """
        This protocol handles indexed retrieval. If the type passed in is
        an integer then return the corresponding list of words from
        self._word_ranks, and if the key isn't in self._word_ranks return
        an empty list.

        Else return the count for the passed in string, returning 0 if the
        string isn't in self._word_count.
        """
        if isinstance(i, int):
            return self._word_ranks.get(i, [])
        if isinstance(i, str):
            return self._word_count.get(i, 0)
        raise TypeError("Invalid index type.")

    def __iter__(self):
        """
        The default interator returned, if iter() is called on the WordRank
        object, should be an iterator for self._word_count.
        """
        return iter(self._word_count)
