'''At the Universal Technological Security Company (UTSC),
a new system is being developed to validate credit card numbers.
The validation process involves checking if a given credit card number
follows a specific pattern. A valid credit card number should meet
the following criteria:

1. The credit card number must consist of exactly 16 digits.
2. The digits must be between 0 and 9 (inclusive).
3. The first digit should be 4.

Write a Python function named is_valid_credit_card that takes a credit card
number as input (a string) and returns True if it's a valid credit card number
based on the rules. If it doesn't meet all the rules, return False.

Example:
    is_valid_credit_card('4234567890123456')
    >>> True

    is_valid_credit_card('22345678901234567')
    >>> False

Here are the concepts you might need to use to solve this question:
    - String indexing
    - String methods (len, isdigit)
    - If statements

Don't forget to check your code by running a few examples, including the ones
given above. '''

def is_valid_credit_card(card_num):
    ''' PLEASE WRITE BELOW THIS COMMENT '''
