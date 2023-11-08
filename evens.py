def even_number_of_evens(numbers):
    """
    Should raise a TypeError if a list is not passed into the function
    error message: "A list was not passed into the function" 
    If numbers is empty return False
    If the number of even numbers is odd, return False
    If the number of even numbers is 0, return False
    If the number of even numbers is even, return True
    """

    # if isinstance(numbers, list):
    #     return True
    # else:
    #     raise TypeError("A list was not passed into the function")

    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])

        return True if evens and evens % 2 == 0 else False       
    else:
        raise TypeError("A list was not passed into the function")

# When Python runs a file directly, it names it __main__ and any code beneath the if statement will only
# be run if the name of the file is __main__ so when we run the test file it will have the name of __main__ and this
# code won't be run, but when we run this file it will have the name __main__ and it will run this code.
if __name__ == '__main__':
    print(even_number_of_evens(5))