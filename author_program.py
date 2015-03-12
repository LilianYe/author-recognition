import author_functions, os.path

def get_valid_filename(msg):
    """ (str) -> str

    Prompt the user, using msg, to type the name of a file. This file should 
    exist in the same directory as the starter code. If the file does not
    exist, keep re-prompting until they give a valid filename.
    Return the name of that file.
    """
    
    filename = input(msg)
    # use os.path.isfile instead of os.path.exists
    # to make sure it's a file rather than a directory
    while not os.path.isfile(filename):
        print("That file does not exist.")
        filename = input(msg)

    return filename
    
    
def get_valid_directory_name(msg):
    """ (str) -> str

    Prompt the user, using msg, to type the name of a directory. If
    the directory does not exist, keep re-prompting until they give a valid
    directory. 
    Return the name of that directory.
    """
      
    dirname = input(msg)

    while not os.path.isdir(dirname):
        print("That directory does not exist.")
        dirname = input(msg)

    return dirname

### Provided helper function ###    
    
def read_signature(filename):
    """ (str) -> list

    Read a linguistic signature from filename and return it as 
    a list of features. 
    """
    
    sig_file = open(filename, 'r')

    # Read the first feature.
    result = [sig_file.readline().strip()]
    
    # Read each remaining feature and convert each one to float.
    for line in sig_file:
        result.append(float(line.strip()))

    sig_file.close()

    return result    
    
    
# #############################
# The main program begins here 
# #############################

if __name__ == '__main__':

    prompt = 'Enter the name of the file with unknown author: '
    mystery_filename = get_valid_filename(prompt)

    prompt = 'Enter the name of the directory of signature files: '
    dir_name = get_valid_directory_name(prompt)

    # Every file in the dir_name directory must be a linguistic signature. 
    # We assume there is a minimum of one file.
    files = os.listdir(dir_name)

    # ####################################################################
    # The following code parses the mystery file and calculates its 
    # linguistic signature.                                         
    # ####################################################################

    mystery_file = open(mystery_filename, 'r')
    # readlines() gives us a list of strings, one for each line of the file
    text = mystery_file.readlines()
    mystery_file.close()

    # Calculate the signature for the mystery file
    mystery_signature = [mystery_filename]
    mystery_signature.append(author_functions.avg_word_length(text))
    mystery_signature.append(author_functions.type_token_ratio(text))
    mystery_signature.append(author_functions.hapax_legomena_ratio(text))
    mystery_signature.append(author_functions.avg_sentence_length(text))
    mystery_signature.append(author_functions.avg_sentence_complexity(text))
    
    # ####################################################
    # The following code reads the linguistic signatures, 
    # compares them with the mystery_signature,           
    # and reports the author that was the best match.					
    # ####################################################
    
    # Weights of linguistic features.
    weights = [0, 11, 33, 50, 0.4, 4]
    
    # We assume there is at least one signature in the dir_name directory
    this_file = files[0]
    signature = read_signature(dir_name + "/" + this_file)
    best_score = author_functions.compare_signatures(mystery_signature,
                                                     signature, weights)
    best_author = signature[0]
    
    for this_file in files[1:]:
        signature = read_signature(dir_name + "/" + this_file)
        score = author_functions.compare_signatures(mystery_signature,
                                                    signature, weights)
        if score < best_score:
            best_score = score
            best_author = signature[0]
    
    if type(best_score) != float:
        print("Error! No score could be computed")
    else:
        print("Best author match:", best_author, "with score", best_score)
