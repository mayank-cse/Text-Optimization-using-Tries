class Alphabet():

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.children = {}
        self.addresses = []

    def moveToChild(self, character):
        try :
            return self.children[character]
        except :
            self.children[character] = Alphabet(character)
            return self.children[character]

    def addAddress(self, instance):
        self.addresses.append(instance)


class Trie():

    def __init__(self):
        self.head = Alphabet('')

    def add(self, word, word_pointer):
        current = self.head
        for i in word :
            current = current.moveToChild(i)
            current.addAddress(word_pointer)

    def findLocations(self, word):
        current = self.head
        for i in word:
            try : 
                current = current.children[i]
            except :
                return (False,[], None)
        return (True, current.addresses, current)

    def getAutoCompleteSuggestions(self, word):
        res = self.findLocations(word)
        if not res[0]:
            return []
        suggestions = set([i.content for i in res[1]])
        return suggestions

    def get_terminals(self, ob):
        if ob.addresses!=[]:
            terminals = [ob]
        else :
            terminals = []
        nodes = [ob]
        while(nodes!=[]):
            curr = nodes.pop(0)
            children = curr.children.values()
            terminals.extend(list(filter(lambda x : x.addresses!=[], children)))
            nodes.extend(children)
        terminals_addresses = []
        for i in terminals:
            terminals_addresses.extend(i.addresses)
        return terminals_addresses

    def printAll(self):
        print("\nAll stuff of trie printed\n")
        print("Alpha\tN_end\tChildren")
        alphabets = [self.head]
        while(alphabets!=[]):
            current = alphabets.pop(0)
            print(current.alphabet, len(current.addresses), current.children.keys(), sep="\t")
            alphabets.extend(current.children.values())
        print()
