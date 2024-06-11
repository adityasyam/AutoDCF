from constants import number_of_years, tax_rate, net_revenues_past_year, \
net_revenue_forecasted_growth_rates, COGS_past_year, SGA_past_year, \
amortization_past_year, interest_expense_past_year

import numpy as np

net_revenues_forecasted = np.zeros(number_of_years)
cogs_forecasted = np.zeros(number_of_years)
gross_profit_forecasted = np.zeros(number_of_years)
sga_forecasted = np.zeros(number_of_years)
amort_forecasted = np.zeros(number_of_years)
op_expenses_forecasted = np.zeros(number_of_years)
op_income_forecasted = np.zeros(number_of_years)
interest_expense_forecasted = np.zeros(number_of_years)
net_income_forecasted = np.zeros(number_of_years)

cogs_ratio = COGS_past_year[0]/net_revenues_past_year[0]
sga_ratio = SGA_past_year[0]/net_revenues_past_year[0]
amort_ratio = amortization_past_year[0]/net_revenues_past_year[0]
interest_ratio = interest_expense_past_year[0]/net_revenues_past_year[0]

def income_calc(tax_rate, net_revenue_forecasted_growth_rates, cogs_ratio, sga_ratio, amort_ratio, interest_ratio):
  for i in range(number_of_years):
    if i==0:
      net_revenues_forecasted[i] = net_revenues_past_year[0]*(1+(net_revenue_forecasted_growth_rates[i]/100))
    else:
      net_revenues_forecasted[i] = net_revenues_forecasted[i-1]*(1+(net_revenue_forecasted_growth_rates[i]/100))
  
  return net_revenues_forecasted

income_out = income_calc(tax_rate, net_revenue_forecasted_growth_rates, cogs_ratio, sga_ratio, amort_ratio, interest_ratio)
print(income_out)

  
  
                


