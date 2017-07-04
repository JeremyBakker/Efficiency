def return_max_profit(prices):
    '''
    This function returns the max profit from a hypothetical list of stock 
    prices set out in chronological order.

    ---Arguments---
    prices (list): a list of hypothetical stock prices
    '''
    if len(prices) < 2:
        raise IndexError('There must be at least two prices to compare.')
    max_profit = prices[1] - prices[0]
    min_price = prices[0]
    max_price = prices[0]
    for price in prices:
        possible_return = price - min_price
        max_price = max(price, max_price)
        max_profit = max(max_profit, possible_return)
        min_price = min(price, min_price)
    return max_profit

def binary_search(target, numbers):
    '''
    This function searches for a target number by running a binary search 
    through an ordered list of numbers.
    
    ---Arguments---
    target (integer): an integer to find in a list
    numbers (list): an orderd list of integers
    '''
    lowest_index = -1
    highest_index = len(numbers)

    while lowest_index + 1 < highest_index:
        start_distance = int((highest_index - lowest_index)/2)
        guess_index = lowest_index + start_distance
        guess_value = numbers[guess_index]

        if guess_value == target:
            return True
        if guess_value > target:
            highest_index = guess_index
        else:
            lowest_index = guess_index
    return False

def highest_product_of_three(numbers):
    '''
    This function returns the highest product of three numbers from a list of 
    more than three numbers. It uses a 'greedy' algorithmic approach.

    ---Arguments---
    numbers (list): a list of integers
    '''
    if len(numbers) < 3:
        raise IndexError('The list must contain more than three numbers')

    highest_number = max(numbers[0], numbers[1])
    lowest_number = min(numbers[0], numbers[1])
    highest_two = numbers[0] * numbers[1]
    lowest_two = numbers[0] * numbers[1]
    highest_three = numbers[0] * numbers[1] * numbers[2]

    i = 2
    while i < len(numbers):
        highest_three = max(highest_three, numbers[i] * highest_two, numbers[i] * lowest_two)

        highest_two = max(highest_two, numbers[i] * highest_number, numbers[i] * lowest_number)
        lowest_two = min(lowest_two, numbers[i] * highest_number, numbers[i] * lowest_number)

        highest_number = max(highest_number, numbers[i])
        lowest_number = min(lowest_number, numbers[i])
        i+=1

    return highest_three

def is_unique(string):
    '''This function determines whether a string has all unique characters

    ---Arguments---
    string (string): a string of characters
    '''
    if len(string) == 0:
        raise ValueError('You must input a string of at least one character.')

    character_set = [False for _ in range(128)]
    
    for character in string:
        value = ord(character)

        if character_set[value]:
            return False
        else:
            character_set[value] = True
    return True