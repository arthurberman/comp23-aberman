def count(file):
        f = open(file, 'r')
        dict = {}
        for line in f:
                low = line.lower()
                words = low.rsplit(" ")
                for word in words:
                        if word in dict:
                                dict[word] += 1
                        else:
                                dict[word] = 1
        list = dict.keys()
        list.sort()
        for entry in list:
                print entry, dict[entry]
count('23halloffame')
