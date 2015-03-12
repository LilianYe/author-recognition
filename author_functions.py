##########  Provided helper function. ############

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. 

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """
    
    punctuation = """!"',;:.-?)([]<>*#\n\t\r"""
    result = s.lower().strip(punctuation)
    return result


def text_to_wordslist(text):
    """(list of str) -> (list of list of str)

    Do clean_up for the str in text, then remove all the commas, 
    then change the str into the list of single word 

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> text_to_wordslist(text)
    [['james', 'fennimore', 'cooper'], ['peter', 'paul', 'and', 'mary']]
    >>> text = ['this is great\n', 'This was awesome\n', 'and, what about IS\n']
    >>> text_to_wordslist(text)
    [['this', 'is', 'great'], ['this', 'was', 'awesome'], ['and', 'what', 'about', 'is']]
    """

    text_list = []
    for sentence in text:
        # split the sentence to list of words
        words_list = sentence.split()
        # do clean_up for every word
        words_list = [clean_up(w) for w in words_list]
        # remove empth and blank word
        words_list =  [w for w in words_list if w.strip()]
        text_list.append(words_list)
    return text_list 


def avg_word_length(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text. 
    
    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143 
    >>> text = ['The first linguistic feature is simply the average number\n', 
    'of characters per word,\n', 'calculated after the punctuation has been stripped\n', 
    'using the already-written clean_up function.\n']
    >>> avg_word_length(text)
    6.04
    """
    
    total_length = 0.0
    words_count = 0.0
    texts_list = text_to_wordslist(text)
    for words_list in texts_list:
        words_count += len(words_list)
        for word in words_list:
            total_length += len(word)
    return total_length / words_count 


def type_token_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
        'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    >>> text = ['this is great\n', 'This was awesome\n', 'and, what about IS\n']
    >>> type_token_ratio(text)
    0.8
    """
  
    different_words = set()
    words_count = 0.0
    texts_list = text_to_wordslist(text)
    for words_list in texts_list:
        words_count += len(words_list)
        for word in words_list:
            different_words.add(word)

    return len(different_words)/ words_count

             
def hapax_legomena_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the hapax legomena ratio for text. This ratio is the number of 
    words that occur exactly once divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
    'James Gosling\n']
    >>> hapax_legomena_ratio(text)
    0.7777777777777778
    >>> text = ['this is great\n', 'This was awesome\n', 'and, what about IS\n']
    >>> hapax_legomena_ratio(text)
    0.6
    """
 
    different_words = []
    words_appear_more_than_1 = []    
    words_count = 0.0 
    texts_list = text_to_wordslist(text)
    for words_list in texts_list:
        words_count += len(words_list)
        for word in words_list:
            if word in different_words:
                words_appear_more_than_1.append(word)
            else:
                different_words.append(word)

    return (len(set(different_words)) - len(set(words_appear_more_than_1))) / words_count


def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    >>> split_on_separators("Hooray! Finally, we're done.", "!, ")
    ['Hooray', 'Finally', "we're", 'done.']
    """
    
    result_list = []
    original_list = [original]
    for sep in separators:
        for sentence in original_list:
            for words in sentence.split(sep):
                result_list.append(words)
        original_list = result_list
        result_list = []

    result_list = original_list
    # remove empth and blank strings
    result_list =  [x for x in result_list if x.strip()]
    return result_list
        
def avg_sentence_length(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.
    
    A sentence is defined as a non-empty string of non-terminating 
    punctuation surrounded by terminating punctuation or beginning or 
    end of file. 
    Terminating punctuation is defined as !?.

    Return the average number of words per sentence in text.   

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_length(text)
    17.5
    >>> text = ['Emma Woodhouse, handsome, clever, and rich, with a comfortable home\n',
         'and happy disposition, seemed to unite some of the best blessings of\n',
         'existence? and had lived nearly twenty-one years in the world with very!\n',
         'little to distress or vex her.\n']
    >>> avg_sentence_length(text)
    13.333333333333334
    """
    
    all_sentences = ""
    # make the text to one string
    for sentence in text:
        all_sentences += sentence

    # split the huge string to sentences 
    sentence_list = split_on_separators(all_sentences, '!?.')
    sentence_count = len(sentence_list)
    words_count = 0.0
    for sentence in sentence_list:
        sentence = sentence.replace('\n',' ')
        word_list = sentence.split()
        # clean_up for every word
        word_list = [clean_up(x) for x in word_list]
        # remove empth and blank strings
        word_list =  [x for x in word_list if x.strip()]
        words_count += len(word_list)
        
    return words_count / sentence_count


def avg_sentence_complexity(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.    

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of ,;:

    Return the average number of phrases per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    >>> text = ['Emma Woodhouse, handsome, clever, and rich, with a comfortable home\n',
         'and happy disposition, seemed to unite some of the best blessings of\n',
         'existence? and had lived nearly twenty-one years in the world with very!\n',
         'little to distress or vex her.\n']
    >>> avg_sentence_complexity(text)
    2.6666666666666665
    """
    
    all_sentences = ""
    # make the text to one string
    for sentence in text:
        all_sentences += sentence

    # split the huge string to sentences 
    sentence_list = split_on_separators(all_sentences, '!?.')
    sentence_count = len(sentence_list)
    phrase_count = 0.0
    for sentence in sentence_list:
        # split the sentence to phrases
        phrase_list = split_on_separators(sentence, ',;:')
        # clean_up every phrase
        phrase_list = [clean_up(p) for p in phrase_list]
        # remove empty or blank phrases
        phrase_list = [p for p in phrase_list if p.strip()]
        phrase_count += len(phrase_list)

    return phrase_count / sentence_count

    
    
def compare_signatures(sig1, sig2, weight):
    """ (list, list, list of float) -> float

    Return a non-negative float indicating the similarity of the two 
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.
    
    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007
    >>> sig1 = ['agatha christie', 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ['alexandre dumas', 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    0.0
    """
    
    score = 0.0
    for i in range(1, len(sig1)):
        score += abs(sig1[i]-sig2[i]) * weight[i]

    return score

