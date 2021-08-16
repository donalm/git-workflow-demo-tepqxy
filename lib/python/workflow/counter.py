#!/usr/bin/env python
'''Manage the count.'''


class Counter(object):
    '''Manage the count.'''

    def __init__(self, value):
        '''
        Return an instance of Counter.

        Args:
            value (int): Initial value

        Returns:
            Counter: New instance of Counter

        '''
        self.value = value

    def increment(self):
        '''
        Increment the value.

        Returns:
            int: The new value.

        '''
        self.value += 1
        return self.value


    def decrement(self):
        self.value -= 1
        return self.value
