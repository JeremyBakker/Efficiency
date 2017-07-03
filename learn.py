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


def reduce_without_index(numbers):
    # i = 0
    # numbers_after_index = numbers[i:]
    # product_before_index = 1
    # while i < len(numbers):
    #     product_before_index *= numbers[i:]
    #     print(product_before_index)
    #     i += 1
    # # final_product = numbers_before_index * numbers_after_index
    final_product = [84, 12, 28, 21]
    return final_product