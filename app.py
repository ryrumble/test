'''
Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a
string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam
list to the function would return 'apples, bananas, tofu, and cats'.
But your function should be able to work with any list value passed to it.
Be sure to test the case where an empty list [] is passed to your function.
'''
def format_list(input_list):
    """This function takes a list, and then returns the list to the user."""
    if len(input_list) == 0:
        return "nothing"
    if len(input_list) == 1:
        return input_list[0]
    formatted_items = ', '.join(input_list[:-1])
    return f"{formatted_items}, and {input_list[-1]}"

# Test cases
spam = ['apples', 'bananas', 'tofu', 'cats']
result = format_list(spam)
print(result)  # Output: 'apples, bananas, tofu, and cats'

empty_list = []
result_empty = format_list(empty_list)
print(result_empty)  # Output: ''
