class FullText():

    class Sentence():

        class Word():

            def __init__(self, word, number, begin, s_number, TRIE_OBJ):
                self.content = word
                self.number = number
                self.address_begin = begin
                self.s_number = s_number
                TRIE_OBJ.add(word, self)

            def printAll(self):
                print(self.number, self.address_begin, self.address_begin+len(self.word), self.content, sep="\t") 

        def __init__(self, sentence, number, TRIE_OBJ):
            self.words = []
            self.number = number
            count = 0
            for num, i in enumerate(sentence.split()):
                l = len(i)
                self.words.append(self.Word(i, num, count , self.number, TRIE_OBJ))
                count += l+1

        def printAll(self):
            for i in self.words:
                print(self.number, end="\t")
                i.printAll()

    def __init__(self, text, trie_obj):
        self.TRIE_OBJ = trie_obj
        self.sentences = []
        for num,i in enumerate(text.split("\n")):
            self.sentences.append(self.Sentence(i, num, self.TRIE_OBJ))

    def addSentence(self, text, index):
        self.sentences = self.sentences[:index]+[self.Sentence(text, index, self.TRIE_OBJ)] + self.sentences[index:]
        for i in self.sentences[i:]:
            i.number += 1

    def getByLocation(self, s_index, w_index):
        try :
            return self.sentences[s_index].words[w_index]
        except :
            print("Index out of bounds")
            return None

    def printAll(self):
        for i in self.sentences :
            i.printAll()
