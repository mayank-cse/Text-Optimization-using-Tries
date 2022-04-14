from  Document import Document
import time
import pickle

def main():

    FILE_NAME = "test2.txt"
    doc = None

    # setups
    print("Load earlier model or use new one? (l to load else use new)")
    inp = input()
    if inp=='l' or inp=='L':
        try :
            print("Enter the name of the save file : ", end = "")
            name = input()
            a = time.time_ns()
            doc = pickle.load(open( name+".p", "rb"))
            b = time.time_ns()
            assert type(doc)==type(Document(""))
            print("Model loaded in : ",(b-a),"ns")
        except : 
            print("Error opening model, creating new one")
            with open(FILE_NAME, "r") as t :
                text = t.read()
                a = time.time_ns()
                doc = Document(text)
                b = time.time_ns()
                print("Model initialised in : ",(b-a),"ns")
    else :
        with open(FILE_NAME, "r") as t :
            text = t.read()
            a = time.time_ns()
            doc = Document(text)
            b = time.time_ns()
            print("Model initialised in : ",(b-a)/10**9,"s")

    # printer methods
    def search_results_printer(res):
        if len(res):
            res, l = res[0], res[1]
            print("Node exists . Addresses : " )
            print("S.no.\tW.no.\tBeg.\tEnd")
            for i in res:
                print(i.s_number, i.number, i.address_begin, i.address_begin+l, sep='\t')
        else:
            print("Node doesn't exist")

    def autocomplete_results_printer(res):
        if res==[]:
            print("No suggestions")
        else:
            print("Num.\tSuggestion")
            for num, i in enumerate(res):
                print(num+1,i,sep="\t")


    # user inputs
    print("\nEnter the number of search queries : ", end="")
    n_searches  = int(input())
    for i in range(n_searches):
        print("Enter the",(i+1),"query : ", end="")
        q = input()
        a = time.time_ns()
        res = doc.search(q)
        b = time.time_ns()
        print("\n",len(res[0]),"results fetched in :",(b-a),"ns")
        print("Do you want to print the results? (y for yes, else no)")
        inp = input()
        if inp=='y' or inp=='Y':
            print("\nResults :")
            search_results_printer(res)

    print("\nEnter the number of autocomplete queries : ", end="")
    n_searches  = int(input())
    for i in range(n_searches):
        print("Enter the",(i+1),"query : ", end="")
        q = input()
        a = time.time_ns()
        res = doc.suggestions(q)
        b = time.time_ns()
        print("\n",len(res),"results fetched in :",(b-a),"ns")
        print("Do you want to print the results? (y for yes, else no)")
        inp = input()
        if inp=='y' or inp=='Y':
            print("\nResults :")
            autocomplete_results_printer(res)

    print("\nDo you want to save this model? (y for yes else no)")
    inp = input()
    if inp=='y' or inp=='Y':
        print("Enter your prefereed name for the object : ", end = "")
        name = input()
        a = time.time_ns()
        pickle.dump(doc, open( name+".p", "wb"))
        b = time.time_ns()
        print("Model saved in : ",(b-a),"ns")

if __name__=='__main__':
    main()
