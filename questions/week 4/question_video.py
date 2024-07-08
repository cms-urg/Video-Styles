''' You work at the Universal Techno Service and Consulting (UTSC)
and you are resposible for booking party clubs for our clients.
The two main characteristics of a club are:
    1. Capacity:        The number of guests that can be hosted.
    2. Price:           The cost of booking the club.

You are given a list of club names, their capacities, and prices
(they share the same ordering).

Each club booking request will consist of a guest count and a budget.
A suitable club is one whose capacity is higher than the guest count and
whose price is lower than the budget.

Write a program that takes the request, and prints
the name of a suitable club. If there is no club that
satisfies the booking criteria, print an error message of
your choice. If there are more than one suitable clubs, return
the name of the cheapest of those clubs.

You can take user input with the following command:
    input("some prompt for the user")

Here are the concepts you might need to use to solve this question:
    - Counted for loops
    - If statements

Here is the list of names, capacities, and prices we have created.
Feel free to modify this to test different cases.
'''
names = ['a', 'b', 'c', 'd', 'e']
capacities = [1000, 500, 400, 200, 100]
prices = [10000, 5000, 4000, 2000, 1000]
'''
Example:
    Enter guest count: 450
    Enter budget: 20000
    >>> The best available club is: b

Example:
    Enter guest count: 150
    Enter budget: 1500
    >>> There is no suitable club that satisfies the client's request.
'''
''' PLEASE WRITE BELOW THIS COMMENT '''