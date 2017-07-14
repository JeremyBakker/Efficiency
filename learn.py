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
    '''This function determines whether a string has all unique characters.

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

def is_unique_without_addition(string):
    '''This function determines whether a string has all unique characters 
    without using additional data structures.

    ---Arguments---
    string (string): a string of characters
    '''
    if len(string) > 128:
        return False

    for character in string:
        if string.count(character) > 1:
            return False
    return True


def binary_gap(N):
    '''
    This function, given a positive integer N, returns the length of its 
    longest binary gap. The function returns 0 if N doesn't contain a binary 
    gap.

    ---Arguments---
    N (int): an integer less than 2,147,483,647
    '''
    N = str(bin(N)[2:])
    count = 0
    solution_count = 0
    for x in range(len(N)):
        if N[x] == "0":
            count += 1
        if N[x] == "1":
            solution_count = max(count, solution_count)
            count = 0
    return solution_count

def shift_array(A, K):
    '''
    This function, given a zero-indexed array A consisting of N integers and an 
    integer K, returns the array A rotated K times.

    ---Arguments---
    A (list): a list of integers
    K (int): an integer
    '''
    if len(A) == 1:
        return A
    B = [0 for _ in range(len(A))]
    for i in range(len(A)):
        if i + K > (len(A) - 1):
            B[i + K - len(A)] = A[i]
        else:
            B[i + K] = A[i]
    return B

def integer_pairs(A):
    '''
    This function, given an array A consisting of N integers, returns the value of 
    the unpaired element.

    ---Arguments---
    A (list): a list of integers with one unpaired integer
    '''
    for integer in A:
        if A.count(integer) == 1:
            return integer

def find_missing_element(A):
    '''
    This function, given a zero-indexed array A, returns the value of the 
    missing element in the series.

    ---Arguments---
    A (list): a list of sequential integers missing one element in the sequence
    '''
    xor = len(A) + 1
    for a, i in enumerate(A, 1):
        xor = xor ^ a ^ i
    return xor

def string_compression(string):
    '''
    This function compresses a string of characters, replacing repetitive 
    characters in a series with numbers if the compressed string is shorter 
    than the original string (i.e., string_compression("AAABBCCCC") returns 
    A3B2C4).

    ---Arguments---
    string (string): a string of characters
    '''
    compressed_string = []
    count = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i-1]:
            compressed_string.append(string[i-1] + str(count))
            count = 0
        count +=1

    compressed_string.append(string[-1] + str(count))

    return min(string, "".join(compressed_string), key=len)

def check_permutation(list_of_two_strings):
    '''
    This function determines whether two strings are permutations of each other

    ---Arguments---
    list_of_two_strings (list): a list of two strings
    '''
    str1 = list_of_two_strings[0]
    str2 = list_of_two_strings[1]
    if len(str1) != len(str2):
        return False
    dic = dict()
    for c in str1:
        dic[c] = dic.get(c, 0) + 1
    for c in str2:
        if dic[c] == 0:
            return False
        dic[c] -= 1
    return True

def isSubstring(s1, s2):
    '''
    This function determines whether one string is a substring of another.

    ---Arguments---
    s1(string): a string
    s2(string): a string
    '''
    if len(s1) != len(s2):
        return False
    if sorted(s1) != sorted(s2):
        return False
    if s1 not in (s2 + s2):
        return False
    return True 

def fizzbuzz(n):
    solution = []
    for digit in range(1,n+1):
        if digit % 3 == 0 and digit % 5 == 0:
            solution.append('FizzBuzz')
        elif digit % 3 == 0:
            solution.append('Fizz')
        elif digit % 5 == 0:
            solution.append('Buzz')
        else:
            solution.append(digit)
    return solution

def find_odd_occurrences(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

def findTheDifference(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict ={}
        for letter in s:
            dict[letter] = dict.get(letter, 0) + 1
        for letter in t:
            if dict.get(letter,0) == 0:
                return letter
            else:
                dict[letter] -= 1