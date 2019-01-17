"""
Calculator library containing basic math operations
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term


def divide(first_term, second_term):
    value = None
    try:
        value = first_term / second_term
    except ZeroDivisionError:
        value = None
    return value
