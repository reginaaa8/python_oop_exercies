"""Word Finder: finds random words from a dictionary."""
from random import choices

class WordFinder:

    def __init__(self, file):
        dictionary = open(file)
        self.words = self.parse(dictionary)
        dictionary.close()
        print(f"{len(self.words)} words read")

        #close file after reading

    def parse(self, dictionary):
        return [w.strip() for w in dictionary]
    
    def random(self):
        return choices(self.words)


wf = WordFinder("words.txt")