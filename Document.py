from Content import FullText
from Trie import Trie

class Document():

    def __init__(self, text):
        self.ob_trie = Trie()
        self.ob_text = FullText(text, self.ob_trie)


    def printAllContent(self):
        self.ob_text.printAll()


    def printAllTrie(self):
        self.ob_trie.printAll()


    def search(self, word):
        res = self.ob_trie.findLocations(word)
        if res[0]:
            l = len(word)
            return (res[1],l)
        else :
            return []


    def suggestions(self, substring):
        res = self.ob_trie.getAutoCompleteSuggestions(substring)
        return res
