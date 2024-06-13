import numpy as np

from constants import number_of_years, risk_free_rate, industry_beta, market_risk_premium, \
  terminal_growth_rate, cost_of_debt, tax_rate

from income_statement import forecast_revenues_base, forecast_net_income_base


def stringify(num_array):
  string = ""
  count=0
  for i in num_array:
    if count==len(num_array)-1:
      string+=str(i)+" "
    else:
      string+=str(i)+", "
    count+=1
  return string



str_forecase_revenues_base = stringify(forecast_revenues_base)
print("The forecasted revenues for the years specified are " + str_forecase_revenues_base)

str_forecast_net_income_base = stringify(forecast_net_income_base)
print("The forecasted net income for the years specified is " + str_forecast_net_income_base)

