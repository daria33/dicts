# #!/usr/bin/env python


def count_unique(string1):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}
  
    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    our_dict = {}

    words = string1.split()
    
    for word in words:
        if word in our_dict:
            our_dict[word] = our_dict[word] + 1
        else:
            our_dict[word] = 1

    return our_dict


    words = string1.split()
    d = {}
    for word in words:
        if word in d:
            d[word] = d[word] + 1 
        else:
            d[word] = 1

    return d

    

def common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between 
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    newlist = []

    for word1 in list1:
        for word2 in list2:
            if word1 == word2:
                newlist.append(word1)

    return newlist

    common = []

    for word1 in list1:
        for word2 in list2:
            if word1 == word2:
                common.append(word1)

    return common


def unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between 
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `common_items`, this should find [1, 2]:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show 
    more than 1 or 2 once:

        >>> sorted(unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """


    def isin(lists, element):
        for num in lists:
            if num == element:
                return True
        return False

    common = common_items(list1, list2)

    newlist = []

    for item in common:
        if isin(newlist, item) == False:
            newlist.append(item)

    return newlist



def sum_zero(list1):
    """Return list of x,y number pair lists from a list where x+y==0

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

        
    For example:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together, 
    that's fine, too:

        >>> sort_pairs( sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """


    zerosdict = {}

    zeroslist = []


    for item1 in list1:
        for item2 in list1:
            if item1+ item2 == 0:
                if item1 not in zerosdict and -item1 not in zerosdict:
                    zerosdict[item1]= (-item1)

    zeroslist = zerosdict.items()

    return zeroslist




#     newlist = []
#     finallist = []

#     for i in range(0, len(list1)):
#         for j in range(i, len(list1)):
#             if list1[i] + list1[j] == 0:
#                 if list1[i] not in newlist and -list1[i] not in newlist:
#                     newlist.append(list1[i])

#     for item in newlist:
#         finallist.append([item, -item])

#     return finallist

# ourlist = [1, -1, 5, 6, 7, 8, 7]

# print sum_zero(ourlist)

def find_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(find_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(find_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    myset = set(words)

    return myset


    # mylist = []

    # for word in words:
    #     if word not in mylist:
    #         mylist.append(word)

    # return mylist



    # mylist = []

    # for word in words:
    #     if word  not in mylist:
    #         mylist.append(word)

    # return mylist



def word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length.

    For example:

        >>> word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    ourdict = {}

    for word in words:
        wordlength = len(word)
        if wordlength in ourdict:
            ourdict[wordlength] = ourdict[wordlength] + [word]
        else:
            ourdict[wordlength] = [word]

    return ourdict.items()



#     dicts = {}

#     for word in words:
#         length = len(word)
#         if length in dicts:
#             dicts[length].append(word)
#         else:
#             dicts[length] = [word]

#     return dicts.items()


def adv_word_length_sorted_words(words):
    """Given list of words, return list of ascending [(len, [sorted-words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that 
    word-length, and the list of words of that word length. The list of words
    for that length should be sorted alphabetically.

    For example:

        >>> adv_word_length_sorted_words(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    ourdict = {}

    for word in words:
        wordlength = len(word)
        if wordlength in ourdict:
            ourdict[wordlength] = ourdict[wordlength] + [word]
        else:
            ourdict[wordlength] = [word]

    for key in ourdict:
        ourdict[key] = sorted(ourdict[key])

    return ourdict.items()




#     dicts = {}
#     final_list = []

#     for word in words:
#         length = len(word)
#         if length in dicts:
#             dicts[length].append(word)
#         else:
#             dicts[length] = [word]

#     sorted_keys = sorted(dicts)

#     for key in dicts:
#         dicts[key]= sorted(dicts[key])

#     for key in sorted_keys:
#         final_list.append((key, dicts[key]))

#     return final_list

# mylist = ["daria", "cam", "rabbits"]

# print adv_word_length_sorted_words(mylist)

def pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.
   
    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    piratedict = {}
    new_phrase = []

    phrase_words = phrase.split()

    english = ['sir', 'hotel', 'student', 'boy', 'madam', 'professor', 'restaurant', 'your', 'excuse', 'students','are', 'lawyer', 'the', 'restroom', 'my', 'hello', 'is', 'man']
    pirate = ['matey', 'fleabag inn', 'swabbie', 'matey', 'proud beauty', 'foul blaggart', 'galley', 'yer', 'arr', 'swabbies', 'be', 'foul blaggart', 'th\'', 'head', 'me', 'avast', 'be', 'matey']
  
    for i in range(len(english)):
        piratedict[english[i]] = pirate[i]

    for word in phrase_words:
        if word in piratedict:
            word = piratedict[word]
            new_phrase.append(word)
        else:
            new_phrase.append(word)

    final_phrase = ' '.join(new_phrase)

    return final_phrase


##############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE.


def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d

def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documenttion tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)
 

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "** ALL TESTS PASSED. GOOD WORK!" 
    print