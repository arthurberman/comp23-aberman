import string
def count(file):
        f = open(file, 'r')
        dict = {}
        for line in f:
                low = line.lower()
                words = low.rsplit(" ")
                for wordlit in words:
                        word = ""
                        for ch in wordlit:
                                if(ch in string.ascii_letters):
                                        word += ch

                        if word in dict:
                                dict[word] += 1
                        else:
                                dict[word] = 1
        list = dict.keys()
        list.sort()
        for entry in list:
                print entry, dict[entry]
        print "There are " + str(len(dict)) + " words in this file."
