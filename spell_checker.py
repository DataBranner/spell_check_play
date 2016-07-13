import difflib
import os

class SpellChecker():
    """Rudimentary spell-checker, using difflib.

    TODO: Try Levenshtein (library); order by frequency usage for guesses.
    """
    def __init__(self):
        self.possible_files = [os.path.join('/usr', 'dict', 'words'),
                               os.path.join('/usr', 'share', 'dict', 'words'),
                               os.path.join('/usr', 'share', 'dict', 'web2')]
        self.get_data()

    def get_data(self):
        """Locate UNIX words.txt file and read"""
        self.filename = None
        self.content = None
        for self.filename in possible_files:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as f:
                    self.content = f.read().split()
                break
        self.make_word_dict()

    def make_word_dict(self):
        """Convert content to dict (for future applications)"""
        if self.content:
            self.content = {key: None for key in self.content}

    def check_spelling(self, word):
        """Return boolean: is word in content?"""
        return (word in self.content)

    def find_near_matches(self, word, cutoff=0.999, desired_matches=10):
        """Return list of near-matches"""
        guesses = []
        while cutoff > 0 and len(guesses) < desired_matches:
            cutoff **= 2
            guesses = difflib.get_close_matches(
                    word, self.content, n=desired_matches, cutoff=cutoff)
        return ('cutoff used: {}\n{}'.format(cutoff, guesses))
