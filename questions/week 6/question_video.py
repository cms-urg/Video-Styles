'''You are a part of the UrbanTech Shopping Corp (UTSC)
and you are responsible to create a system to help
customers calculate the amount they need to pay for their purchases.

Write a function that takes two arguments: a dictionary of the product catalog,
which contains all products as keys and their prices as the values,
and a list of products that a customer wishes to buy;
and returns the total amount that the customer has to pay.
Assume that the customer can only purchase 1 quantity of any item that
is present in the catalog.

Example:
    catalog = {'laptop':2000.00, 'mobile':1000.00, 'mouse':25.55}
    cart = ['laptop', 'mouse', 'headphones']
    print("Total cost is: " + str(calculate_cart(catalog, cart)))
    >>> Total cost is: 2025.55

Here are the concepts you might need to solve this question:
    - Dictionaries
    - Elemental for loops
    - If statements

Don't forget to check your code by running a few examples, including the one
given above.
'''
catalog = {'laptop':2000.00, 'mobile':1000.00, 'mouse':25.55}
cart = ['laptop', 'mouse', 'headphones']
def calculate_cart (catalog, cart):
    ''' PLEASE WRITE BELOW THIS COMMENT '''