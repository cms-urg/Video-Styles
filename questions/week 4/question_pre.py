''' You work at the Universal Taste Selection Company (UTSC)
and you are resposible for building a restaurant recommendation system.
The two main characteristics of a restaurant are:
    1. Cuisine:     The type of food that is served by the restaurant
    2. Price:       The average price of an entree at the restaurant

You are given a list of restaurant names, their cuisines and average entree prices
(they share the same ordering).

Each recommendation request will consist of a cuisine and a budget.
A suitable restaurant is one whose average entree price is lower than the budget and
whose cuisine matches the request.

Write a program that takes the request, and prints
the name of a suitable restaurant. If there is no restaurant that
satisfies the request criteria, print the following error message:
    "No restaurant matches your criteria.". 
    
If there are more than one suitable restaurants, print
the name of the restaurant with the cheapest average entree price.

You can take user input with the following command:
    input("some prompt for the user")

Here are the concepts you might need to use to solve this question:
    - Counted for loops
    - If statements

Here is the list of names, capacities, and prices we have created.
Feel free to modify this to test different cases.
'''
names = ['Restaurant A', 'Restaurant B', 'Restaurant C', 'Restaurant D', 'Restaurant E']
cuisines = ['Italian', 'Chinese', 'Mexican', 'Italian', 'Chinese']
prices = [30, 20, 15, 45, 30]
'''
Example:
    Enter cuisine: Chinese
    Enter budget: 25
    >>> Restaurant B

Example:
    Enter guest count: Italian
    Enter budget: 25
    >>> No restaurant matches your criteria.

    FOR YOUR SUBMISSION TO BE GRADED CORRECTLY, YOUR OUTPUT SHOULD ONLY CONTAIN THE NECESSARY OUTPUT, AND NO OTHER PRINT STATEMENTS
'''
''' PLEASE WRITE BELOW THIS COMMENT '''
