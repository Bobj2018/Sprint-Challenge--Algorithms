'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # TBC
    # check if the first two indexes contains 'th', if not, call word, minus the first index
    if len(word) == 0: #Base Case
        return 0

    if word[0:2] == 'th':
        return count_th(word[1:]) + 1
    else:
        return count_th(word[1:])
