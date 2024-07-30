import numpy as np

from constants import number_of_years, risk_free_rate, industry_beta, market_risk_premium, \
  terminal_growth_rate, cost_of_debt, tax_rate, long_term_debt_past_year

from income_statement import forecast_revenues_base, forecast_net_income_base, cogs_forecasted_base, sga_forecasted_base, op_income_forecasted_base

from balance_sheet import dep_amort_base_forecasted, receivables_base_forecasted, inventory_base_forecasted, other_current_assets_base_forecasted, accounts_payable_base_forecasted, accrued_expenses_base_forecasted

from cash_flow_statement import capex_base

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

ebit_base = np.zeros(number_of_years)
ebit_minus_tax = np.zeros(number_of_years)
non_working_capital_changes_base = np.zeros(number_of_years)

fcf_to_firm_base = np.zeros(number_of_years)

def dcf_first_half(market_outlook):
  if market_outlook=="base":
    for i in range(number_of_years):
      ebit_base[i] = op_income_forecasted_base[i]
      ebit_minus_tax[i] = ebit_base[i]*(1-(tax_rate/100))
      non_working_capital_changes_base[i] = ebit_minus_tax[i]+dep_amort_base_forecasted[i]+capex_base[i]

def dcf_working_capital_changes(market_outlook):
  if market_outlook=="base":
    net_changes_in_working_cap = np.zeros(number_of_years)
    for i in range(number_of_years):
      net_changes_in_working_cap[i] = receivables_base_forecasted[i]+inventory_base_forecasted[i]+other_current_assets_base_forecasted[i]-accounts_payable_base_forecasted[i]-accrued_expenses_base_forecasted[i]

    return net_changes_in_working_cap
  
working_cap_changes_base = dcf_working_capital_changes("base")


fcf_to_firm_base = non_working_capital_changes_base+working_cap_changes_base

cost_of_equity = industry_beta + ((market_risk_premium/100)*(risk_free_rate/100))

pv_factors = np.zeros(number_of_years)

for i in range(number_of_years):
  if i==0:
    pv_factors[i]=1/(1+cost_of_equity)
  else:
    pv_factors[i]=pv_factors[i-1]*pv_factors[0]

fcf_pv_base = fcf_to_firm_base*pv_factors

sum_pv_fcf_base = fcf_pv_base.sum()

terminal_value_base = (fcf_pv_base[-1]*(1+(terminal_growth_rate/100)))/(cost_of_equity/100-terminal_growth_rate/100)

firm_value_base = sum_pv_fcf_base+terminal_value_base

firm_equity_value_base = firm_value_base-long_term_debt_past_year[0]

print("The total equity value of the firm is " + str(firm_equity_value_base))



