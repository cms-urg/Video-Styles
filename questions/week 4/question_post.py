''' You work at the Universal Talent Search Company (UTSC),
which provides skilled workers an online platform to
find suitable opportunities, rate companies, and forums for discussions.

To help improve the job search, you wish to implement a filtering feature.
Users can choose a minimum job rating and a minimum salary. The filter
should only show jobs that have a higher rating and salary than what the
user set.

You are given a list of jobs, their average rating on a scale of 1 to 10, 
and the average salary they offer (they share the same ordering).

Write a program that asks the user for the filters, and prints a list
of all jobs that satisfy the criteria outlined above. If there is no job
that satisfies the criteria, print the following error message:
    "No job matches your criteria"

Here are the concepts you might need to use to solve this question:
    - Counted for loops
    - lists
    - If statements

Here is the list of jobs and their ratings and salaries you have.
Feel free to modify this to test different cases.
'''
jobs = ['joojle - analyst', 'HHM - senior associate', 'warmart - cashier', 'stapler - sales rep', 'banana - developer']
ratings = [7.4, 3.7, 6.1, 9.3, 8.5]
salaries = [100000, 250000, 40000, 45000, 150000]
'''
Example:
    Enter minimum job rating: 9.5
    Enter minimum job salary: 20000
    No job matches your criteria

Example:
    Enter minimum job rating: 7
    Enter minimum job salary: 50000
    ['joojle - analyst', 'banana - developer']

    FOR YOUR SUBMISSION TO BE GRADED CORRECTLY, YOUR OUTPUT SHOULD ONLY CONTAIN THE NECESSARY PRINT STATEMENT
'''
''' PLEASE WRITE BELOW THIS COMMENT '''