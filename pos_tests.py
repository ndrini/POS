# import matplotlib as plt
# from pos_data import pos_all
# import random

# import numpy as np
# import pytest

from pos import Comparation

# def __init__(self, expense_mean, expense_sd, expense_number):
#     self.expense_mean = expense_mean
#     self.expense_sd = expense_sd
#     self.expense_number = expense_number

# def simulation(self):
#     for pos in all_pos:
#        pass

# EXPENSES

# @pytest.mark.parametrize('expense_mean,expense_sd,expense_number', EXPENSES)    def
# def test_expense_generate(self):
#     c = Comparation():
# º
#         mu, sigma = 0, 0.2 # mean and standard deviation
#         s = numpy.random.normal(mu, sigma, 1000)


#     pass

def test_obj_init():
    c = Comparation(
        expense_mean=[1, 2, 3, 4,],  # list
        expense_sd=[4, 3, 2, 1, ],
        expense_number=[10, 20, 30, 40,],
    )
    assert len(c.expense_mean)== 4 

