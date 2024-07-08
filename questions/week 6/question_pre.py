'''You are a part of the Universal Temperature Seruveillance Corp [UTSC]
and you are responsible to create a system to find the most extreme temperatures.

Write a function that takes one argument: a dictinary where the keys are names of some heavily populated cities
and for each city the corresponding value is a list of average daytime temperatures for the last week of that city.
 Your function must return the highest and lowest temperatures (in that order) as a list.

Example:
    temperatures = {'Adelaide': [17, 18, 17, 21, 24, 22, 19], 'Toronto': [14, 7, 7, 6, 4, 11, 15]}
    print("Extreme temperatures of the past week: " + str(get_extremes(temperatures)))
    >>> Extreme temperatures of the past week: [24, 4]

Here are the concepts you might need to solve this question:
    - Dictionaries
    - Elemental for loops
    - If statements

Don't forget to check your code by running a few examples, including the one
given above.
'''
temperatures = {'Adelaide': [17, 18, 17, 21, 24, 22, 19], 'Toronto': [14, 7, 7, 6, 4, 11, 15]}
def get_extremes (temperatures):
    ''' PLEASE WRITE BELOW THIS COMMENT '''