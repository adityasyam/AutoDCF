from constants import number_of_years, tax_rate, net_revenues_past_year, \
net_revenue_forecasted_growth_rates, COGS_past_year, SGA_past_year, \
amortization_past_year, interest_expense_past_year

import numpy as np

cogs_ratio = COGS_past_year[0]/net_revenues_past_year[0]
sga_ratio = SGA_past_year[0]/net_revenues_past_year[0]
amort_ratio = amortization_past_year[0]/net_revenues_past_year[0]
interest_ratio = interest_expense_past_year[0]/net_revenues_past_year[0]


def income_calc(net_revenue_forecasted_growth_rates):
  net_revenues_forecasted = np.zeros(number_of_years)
  cogs_forecasted = np.zeros(number_of_years)
  gross_profit_forecasted = np.zeros(number_of_years)
  sga_forecasted = np.zeros(number_of_years)
  amort_forecasted = np.zeros(number_of_years)
  op_expenses_forecasted = np.zeros(number_of_years)
  op_income_forecasted = np.zeros(number_of_years)
  interest_expense_forecasted = np.zeros(number_of_years)
  net_income_forecasted = np.zeros(number_of_years)

  for i in range(number_of_years):
    if i==0:
      net_revenues_forecasted[i] = net_revenues_past_year[0]*(1+(net_revenue_forecasted_growth_rates[i]/100))
    else:
      net_revenues_forecasted[i] = net_revenues_forecasted[i-1]*(1+(net_revenue_forecasted_growth_rates[i]/100))

  for i in range(number_of_years):
    cogs_forecasted[i] = net_revenues_forecasted[i]*cogs_ratio
    gross_profit_forecasted[i] = net_revenues_forecasted[i] - cogs_forecasted[i]
    sga_forecasted[i] = net_revenues_forecasted[i] * sga_ratio
    amort_forecasted[i] = net_revenues_forecasted[i] * amort_ratio
    op_expenses_forecasted[i] = sga_forecasted[i]+amort_forecasted[i]
    op_income_forecasted[i] = gross_profit_forecasted[i]-op_expenses_forecasted[i]
    interest_expense_forecasted[i] = net_revenues_forecasted[i] * interest_ratio
    net_income_forecasted[i] = (1-(tax_rate/100))*(op_income_forecasted[i] - interest_expense_forecasted[i])
  
  
  return net_revenues_forecasted, net_income_forecasted, cogs_forecasted, sga_forecasted


forecast_revenues_base, forecast_net_income_base, cogs_forecasted_base, sga_forecasted_base = income_calc(net_revenue_forecasted_growth_rates)

forecast_revenues_base = np.round(forecast_revenues_base, 2)
forecast_net_income_base = np.round(forecast_net_income_base, 2)


  
  
                


