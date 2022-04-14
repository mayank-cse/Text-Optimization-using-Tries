from Document import Document
from LinearModel import LinearModel
import time
# from pympler import asizeof
import tracemalloc

def test(f_name, s_queries, a_queries):

    # declarations of the structures
    doc = None
    lin = None

    # reading an inputing the file
    with open(f_name, "r") as t:
        text = t.read()
        # print(text)
        t_doc_beg = time.time_ns()
        doc = Document(text)
        t_doc_end = time.time_ns()
        t_lin_beg = time.time_ns()
        lin = LinearModel(text)
        t_lin_end = time.time_ns()

        print("\nDocument stats : ")
        print("Lines  :  ", len(text.split("\n")))
        print("Words  :  ", len(text.split()))
        print("\nTime to setup : ")
        print("Document model : ", (t_doc_end-t_doc_beg),"ns")
        print("Linear model   : ", (t_lin_end-t_lin_beg),"ns")
        # print("\nSize of objects in memory : ")
        # print("Document model : ", asizeof.asizeof(doc)/(1024*1024),"MB")
        # print("Linear model   : ", asizeof.asizeof(lin)/(1024*1024),"MB")
        print("\n")

    # validation of structure construction
    # print("\n Text Added! Now launching printAll() \n")
    # print("S.no.\tW.no.\tBeg.\tEnd\tContent")
    # doc.printAllContent()
    # print("\n Now analysing the generated \n")
    # doc.printAllTrie()

    # validation of structure functionality

    def search_results_printer(res):
        if len(res):
            res,l = res[0], res[1]
            print("Node exists . Addresses : " )
            print("S.no.\tW.no.\tBeg.\tEnd")
            # for i in res:
            #     print(i.s_number, i.number, i.address_begin, i.address_begin+l, sep='\t')
            print(len(res),"results fetched.")
        else:
            print("Node doesn't exist")

    def linear_search_results_printer(res):
        if len(res):
            print("Node exists . Addresses : " )
            print("S.no.\tW.no.\tBeg.\tEnd")
            # for i in res:
            #     print(i[0], i[1], i[2], i[3], sep='\t')
            print(len(res),"results fetched.")
        else:
            print("Node doesn't exist")

    def autocomplete_results_printer(res):
        if res==[]:
            print("No suggestions")
        else:
            print("Num.\tSuggestion")
            # for num, i in enumerate(res):
            #     print(num+1,i,sep="\t")
            print(len(res),"results fetched.")

    print("Search queries : ")
    for i in s_queries:
        print("Query : ", i)
        print("Document model results\n------------")
        a = time.time_ns()
        res1 = doc.search(i)
        b = time.time_ns()
        search_results_printer(res1)
        print("Time : ",(b-a),"ns")
        print("\nLinear model results\n------------")
        c = time.time_ns()
        res2 = lin.search(i)
        d = time.time_ns()
        linear_search_results_printer(res2)
        print("Time : ",(d-c),"ns")

    print("\n-----\nAutocomplete queries : ")
    for i in a_queries:
        print("Query : ", i)
        print("Document model results\n------------")
        e = time.time_ns()
        res1 = doc.suggestions(i)
        f = time.time_ns()
        autocomplete_results_printer(res1)
        print("Time : ",(f-e),"ns")
        print("\nLinear model results\n------------")
        g = time.time_ns()
        res2 = lin.suggester(i)
        h = time.time_ns()
        autocomplete_results_printer(res2)
        print("Time : ",(h-g),"ns")

    # for the purpose of storage comparison
    # return [lin, doc]

class Test():
    def __init__(self, name, file_name, s_queries, a_queries):
        self.name = name
        self.file_name  = file_name
        self.s_queries = s_queries
        self.a_queries = a_queries
        self.objs = None

    def conduct(self):
        # tracemalloc.start()
        print("\n--------------------------------\n",self.name,"\n--------------------------------")
        # self.objs = test(self.file_name, self.s_queries, self.a_queries)
        test(self.file_name, self.s_queries, self.a_queries)
        # current, peak = tracemalloc.get_traced_memory()
        # print(f"Peak RAM usage was {peak / 10**6}MB")
        # tracemalloc.stop()
        print("\n--------------------------------\n")

if __name__=='__main__':
    t1 = Test("Test 1 : 4 lines ", "test1.txt", ["the","something"], ["the","some"])
    t2 = Test("Test 2 : King James Bible", "test2.txt", ["the","something"], ["the","some"])
    t3 = Test("Test 3 : World Factbook 1992 README", "test3.txt", ["the","something"], ["the","some"])
    # t4 = Test("Test 4 : King James Bible x3 ", "test4.txt", ["something"], ["some"])

    t1.conduct()
    t2.conduct()
    t3.conduct()
    # t4.conduct()
