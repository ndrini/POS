# 1. Aim

This script provides a simulation of different cost senarios bases on a fix cost more variable costs for a service. 

The script creates a consumption senario (or in the specific case an income senario) based on the user experience. 

The script name is derived by point of sale (POS), aka the payment terminal (and, in wider sense) the ecosystems. 

# 1.1 Example 
Let's concider a restaurant that provides also bar services. And try to find the most economic POS (the one with lowest percentage of cost for the restaurant tender).

This script allows to simulate differenc income senarios: 

- the bar: small and frequent amounts 
- the restaurant: bigger than the bar but less frequent ammounts



# 2. Use

## 2.1 Necessary actions

- fill the service dictionary: called pos_data
- provide the senarios: the statistic value for different data cluster
  

For isntace the following data can represent: 

    c = Comparation(
        expense_mean=[4.5, 35],  # mean of bar and restaurant expenses
        expense_sd=[3, 15],
        expense_number=[400, 150],
    )

first column: breakfast (4,5 € mean expense)
second column: dinner (35 € mean expense)


# 3. Run 

    python pos.py


# 4. Tests 

    pytest pos_tests.py