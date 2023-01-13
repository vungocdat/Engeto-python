# main function
def calculator():
    """
    main function
    """
    selection = ('+', '-', '*', '/', 'pow', 'avg', 'quit')
    show_selection(selection)


# selection listing
def show_selection(*args):
    """
    Description:
    connect values from args with .join method
    then add separator between them

    Example:
    args = ("a", "b". "c")

    Result:
    ---------
    a | b | c
    ---------
    """
    joined = ' | '.join(*args)
    separator = '-' * len(joined)
    print(separator, joined, separator, sep='\n')


if __name__ == '__main__':
    calculator()
