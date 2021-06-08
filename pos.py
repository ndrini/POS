import matplotlib.pyplot as plt
# import random
import numpy as np
import pprint

from pos_data import pos_all


class Comparation():
    ''' provide a outlook for a simulation of payment structure '''

    def __init__(self, expense_mean, expense_sd, expense_number):
        self.expense_mean = expense_mean
        self.expense_sd = expense_sd
        self.expense_number = expense_number

    def expense_generate(self) -> list:
        ''' create sintetic expense for the shop'''
        values = []

        for i in range(len(self.expense_mean)):
            mu, sigma = self.expense_mean[i], self.expense_sd[i]
            s = np.random.normal(mu, sigma, self.expense_number[i])
            values.append(s)

        # from list of list to a list
        values = [t if t > 0 else 1 for i in values for t in i]
        return values

    def simulation(self) -> dict:
        ''' main method '''
        expense_syntetic = self.expense_generate()

        # provide a preview of the syntetic data used
        expense_extract = list(
            map(lambda x: round(x, 2),
                expense_syntetic[: min(round(len(expense_syntetic)/10), 20)]))
        msg = 'Extract of the data used for the simulation'
        if expense_extract:
            print(msg)
            pprint.pprint(expense_extract)

        # initialize the response
        pos_res = {'costs': [],
                   'total_gross': round(sum(expense_syntetic), 2),
                   }
        ''' expected structure of pos_res (with example number)
        pos_res = {'total_gross': 2322,
               'costs': [
                   {'name': 'mypos_eu',
                    'total_cost': 225,
                    'real_percent': 5.5, },
                   {'name': 'sdfa',
                    'total_cost': 289,
                    'real_percent': 6, },
               ]}
        '''

        for pos in pos_all:
            # compute the cost for each pos
            total_cost = pos['inital']/12
            for payment in expense_syntetic:
                total_cost += (
                    pos['percent'] * payment / 100 + pos['fix'])
            single_pos_dict = {
                'name': pos['name'],
                'total_cost': round(total_cost, 2),
                'real_percent': round(total_cost/sum(expense_syntetic)*100, 2)}

            pos_res['costs'].append(single_pos_dict)

        self.simulation_show(pos_res)
        pprint.pprint(pos_res)
        return pos_res

    @staticmethod
    def simulation_show(result_dict):
        ''' show data by plotting stat values'''
        column_names = [case['name'] for case in result_dict['costs']]
        total_costs = [case['total_cost'] for case in result_dict['costs']]
        plt.bar(column_names, total_costs)
        plt.title(
            f"Cost over a revenue of {result_dict['total_gross']:5.2f} €")
        plt.ylabel('Total cost of payment system')
        plt.xlabel('Payment names')
        plt.savefig('comparation.png', dpi=300)
        plt.show()


if __name__ == '__main__':

    ''' provide a list of expected value 
    of payment, to inialize the model 
    mean, standard deviation and total payment actions
    '''
    c = Comparation(
        expense_mean=[4.5, 35],  # list
        expense_sd=[3, 15],
        expense_number=[400, 150],
    )
    # expense_values_list = c.expense_generate()
    # pprint.pprint(expense_values_list)
    # print(np.mean(expense_values_list))

    c.simulation()
