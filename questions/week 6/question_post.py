'''You are a TA at UTSC, and your professor has asked you to help them generate a list
of students that have passed the course.

Write a function that takes one argument: a dictinary where the keys are names of the students
and for each student the corresponding value is a list of their assignment grades (in percentage)
Your function must return a list of student names whose assignment average is at least 50%.

Example:
    grades = {'Abby': [70, 80, 90], 'Tom': [30, 70, 40]}
    print("Students that past the course: " + str(get_passing_students(grades)))
    >>> Students that passed the course: ['Abby']

Here are the concepts you might need to solve this question:
    - Dictionaries
    - Elemental for loops
    - If statements

Don't forget to check your code by running a few examples, including the one
given above.
'''
grades = {'Abby': [70, 80, 90], 'Tom': [30, 70, 40]}
def get_passing_students (grades):
    ''' PLEASE WRITE BELOW THIS COMMENT '''