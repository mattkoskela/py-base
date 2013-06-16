##
# This file contains an example class for namespace.pybase
#
# @package     namespace.pybase
# @author      Matt Koskela <mattkoskela@gmail.com>
##

"""
Example.py

This file contains an example class with a basic function.
"""


class Math():
    """
    This is the example Math class in pybase
    """

    def __init__(self):
        self.reset()

    def add_stuff(self, *args):
        """ This function returns the sum of its arguments """

        for arg in args:
           self.total = self.total + arg 

    def reset(self):
        self.total = 0
