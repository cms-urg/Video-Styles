'''We are the Universal Telecom Solutions Corporation (UTSC).
We want to issue new phone numbers to users and to do so, we need your
help to write a program to check the validity of these phone numbers
as per the license issued to our organization.

Write a function that, given a phone number as a string, checks if it is a valid
phone number and returns true if it is or false otherwise.

A valid phone number consists of the following:
1. All characters in the input string are digits
2. The input string contains no spaces
3. The input string has exactly 10 characters
4. The input string does not begin with the digit 0
5. The input string ends with the digits 91

Examples:
    >>> validate_phone_number('9874785291')
    True

    >>> validate_phone_number('2344774591')
    True

    >>> validate_phone_number('0148875591')
    False
    
    >>> validate_phone_number('614887G591')
    False

Here are the concepts you might need to use to solve this question:
    - Boolean variables
    - Elemental for loop
    - If statements

Don't forget to check your code by running a few examples, including the ones
given above. '''

def validate_phone_number(phone_num):
    ''' PLEASE WRITE BELOW THIS COMMENT '''
