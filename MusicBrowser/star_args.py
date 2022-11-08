# def average(*args):
#     print(type(args))
#     print("args is {}:".format(args))
#     print("*args is:", *args)
#     mean = 0
#     for arg in args:
#         mean += arg
#     return mean / len(args)
#
#
# print(average(1, 2, 3))

# ========= challenge 1 =========
# create a function that takes a number of variables and returns a tuple


# def build_tuple(*args):
#     return args
#
#
# message_tuple = build_tuple("hello", "planet", "earth", "take", "me",
#                             "to", "your", "leader")
# print(type(message_tuple))
# print(message_tuple)
#
# number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
# print(type(number_tuple))
# print(number_tuple)

# ========= challenge 2 =========
# a function that takes a variable number of words, and returns the average word length


# def average_word(*args):
#     mean = 0
#     for arg in args:
#         word_len = len(arg)
#         mean += word_len
#
#     return mean / len(args)
#
#
# words = average_word("one", "three", "apple", "orange", "done")
# print(words)

# ========= challenge 3 =========
# A function that returns the smallest or largest of the numbers passed to it.

# def min_lot(extreme=min, *args):
#     if extreme == max:
#         return max(args)
#     elif extreme == min:
#         return min(args)
#     else:
#         print("this function only works if you specify min or max")
#
#
# minmax = min_lot(2, 5, 6, 7, 9, 30, 45)
# print(minmax)

# ========= challenge 4 =========
# A function to print all the words passed to it backwards in revers order.
# so the output will read correctly from right to left


# def reverse(*args):
#     string = ""
#     for arg in args:
#         string += arg
#     return string[::-1]
#
#
# feed = reverse("apples", "wolf", "sheep")
# print(feed)

# courses version
# def print_backwards(*args):
#     for word in args[::-1]:
#         print(word[::-1], end=' ')
#
#
# print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader")

# ========= challenge 5 =========
# Create a list, let's call it words. print the list, but also print *words,
# to see that * can be used to unpack a list as well as a tuple.

# numbers = ["first", "second", "third", "forth", "fifth"]
# print(numbers)
# print(*numbers)


# ======= **kwargs =========

# def print_backwards(*args, **kwargs):
#     # keys = kwargs.keys()
#     # print(kwargs)
#     # print(type(kwargs))
#     # for key in keys:
#     #     if key == 'end':
#     #         remove_key = key
#     #     else:
#     #         remove_key = None
#     #
#     # if remove_key:
#     #     del kwargs[remove_key]
#
#     # kwargs.pop('end', None)
#     end_character = kwargs.pop('end', '\n')
#     sep_character = kwargs.pop('sep', ' ')
#
#     for word in args[::-1]:
#         print(word[::-1], end=sep_character, **kwargs)
#     print(end=end_character)
#
#
# with open("backwards.txt", 'w') as backwards:
#     print_backwards("hello", "planet", "earth", "take", "me", "to", "your",
#                     "leader", end='\n')
#     print("Another string")
#
# print()
# print("hello", "planet", "earth", "take", "me", "to", "your", "leader",
#       end='\n', sep='|')
# print_backwards("hello", "planet", "earth", "take", "me", "to", "your",
#                 "leader", end='\n')


# =========== recommended way =============
def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)

    print(args[0][::-1], end=end_character, **kwargs)


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your",
                    "leader", end='\n')
    print("=" * 70)
    backwards_print("hello", "planet", "earth", "take", "me", "to", "your",
                    "leader", end='\n')
    print("another String")






























