import builtins

def disable_input(*args):
    raise Exception("You should not call input!")

builtins.input = disable_input

import author_functions

def approx(v1, v2):
    """ (float, float) -> bool

    Return True iff v1 and v2 are approximately equal.
    """

    return v1-0.0001 < v2 < v1+0.0001


# Test avg_word_length.
text = [
    "James Fennimore Cooper\n",
    "Peter, Paul, and Mary\n",
]
error_message = "average_word_length on the text:\n\n" + repr(text) + \
    "\n\n should return 5.142857142857143"
assert approx(author_functions.avg_word_length(text), 5.142857142857143),\
    error_message


# Test type_token_ratio.
text = [
    "James Fennimore Cooper\n",
    "Peter, Paul, and Mary\n",
    "James Gosling\n"
]

error_message = "type_token_ratio on the text:\n\n" + repr(text) + \
    "\n\n should return 0.8888888888888888"
assert approx(author_functions.type_token_ratio(text), 0.8888888888888888),\
       error_message

# Test hapax_legomena_ratio.
error_message = "hapax_legomena_ratio on the text:\n\n" + repr(text) + \
    "\n\n should return 0.7777777777777778"
assert approx(author_functions.hapax_legomena_ratio(text),
              0.7777777777777778),error_message

# Test split_on_separators.
hooray = "Hooray! Finally, we're done."
thesplit = ['Hooray', ' Finally', " we're done."]

error_message = "split_on_separators(" + repr(hooray) + \
    ", '!,') should return " + repr(thesplit)
assert author_functions.split_on_separators(hooray, "!,") == thesplit,\
    error_message


# Test avg_sentence_length.
text = ["The time has come, the Walrus said\n",
        "To talk of many things: of shoes - and ships - and sealing wax,\n",
        "Of cabbages; and kings.\n",
        "And why the sea is boiling hot;\n",
        "and whether pigs have wings.\n"]

error_message = "avg_sentence_length on the text:\n\n" + repr(text) + \
    "\n\n should return 17.5"
assert approx(author_functions.avg_sentence_length(text), 17.5),\
    error_message


# Test avg_sentence_complexity.
error_message = "avg_sentence_complexity on the text:\n\n" + repr(text) + \
    "\n\n should return 3.5"
assert approx(author_functions.avg_sentence_complexity(text), 3.5), \
     error_message


# Test compare_signatures.
sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]

error_message = "compare_signatures on signatures \n" + repr(sig1) + "\n" + \
    repr(sig2) + "\n should return 12.000000000000007"
assert approx(author_functions.compare_signatures(sig1, sig2, weight),
              12.000000000000007), error_message


print("okay")
