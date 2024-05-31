"""Word Finder: finds random words from a dictionary."""


class WordFinder:

    def __init__(self, file):
        dictionary = open(file)
        self.words = self.parse(dictionary)
        print(f"{len(self.words)} words read")

    def parse(self, dictionary):
        return [w.strip() for w in dictionary]
    
    def random(self):


wf = WordFinder("words.txt")