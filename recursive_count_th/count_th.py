'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    counter = 1
    if len(word) >= 2:
        if word[:2] == 'th':
            counter += 1
            return 1 + count_th(word[counter:])
        else:
            return count_th(word[counter:])
    return 0


print(count_th("theduckthe"))
