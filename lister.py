def list_maker(a_list, column_number, input):
    """Returns refined list of lists from a larger list of lists, comprised of indeces identified by the user as parameters"""
    '''The function's column_number argument is the column number you are targeting, and the input argument is the string value which resides in the aforementioned column'''
    #test
    new_list = []
    for row in a_list:
        value = row[index]
        if value == input:
            new_list.append(row)
    return new_list 