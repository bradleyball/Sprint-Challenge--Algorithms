'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# takes in a string
# finds how many times "th" is in the word
# needs to use recurrsion

# plan:
# keep an outer function with count as a non local
# for inner fuction have a base case that word < 2 then return
# check to see if last two letters of the word have th, if so increment count
# pass the word in without the last two letters
# else if the last two words are not th, pass in the word without the last letter
# return count


def count_th(word):

    count = 0

    def recurr(word):
        if len(word) < 2:
            return
        if word[-2:] == "th":
            nonlocal count
            count = count + 1
            recurr(word[:-2])
        else:
            recurr(word[:-1])
    recurr(word)
    return count


arr = "theorthasdfthasdfthasaathasdfasdfthasdfth"
print(count_th(arr))
