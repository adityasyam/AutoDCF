from constants import number_of_years, cash_past_year, receivables_past_year, \
inventory_past_two_years, other_current_assets_past_year, ppe_past_two_years, intangible_assets_past_year, \
other_long_term_assets_past_year, accounts_payable_past_year, income_taxes_payable_past_year, \
accrued_expenses_past_year, other_current_liabilities_past_year, long_term_debt_past_year, \
other_long_term_liabilities_past_year, preferred_stock_past_year, common_stock_past_year, \
apic_past_year, retained_earnings_past_year, treasury_stock_past_year, net_revenues_past_year, \
COGS_past_year, SGA_past_year, dividends_past_year, net_income_past_year, depreciation_and_amortization_past_year

from income_statement import forecast_revenues_base, forecast_net_income_base, cogs_forecasted_base, sga_forecasted_base

import numpy as np

receivables_ratio = net_revenues_past_year[0]/receivables_past_year[0]
inventory_ratio = COGS_past_year[0]/inventory_past_two_years[1]
prepaid_expenses_ratio = SGA_past_year[0]/other_current_assets_past_year[0]
payables_ratio = (COGS_past_year[0]+inventory_past_two_years[1]-inventory_past_two_years[0])/accounts_payable_past_year[0]
accrued_expenses_ratio = SGA_past_year[0]/accrued_expenses_past_year[0]
long_term_debt_ratio = net_revenues_past_year[0]/long_term_debt_past_year[0]
other_long_term_liabilities_ratio = net_revenues_past_year[0]/other_long_term_liabilities_past_year[0]
dividends_ratio = dividends_past_year[0]/net_income_past_year[0]

capex_past_year = ppe_past_two_years[1]-ppe_past_two_years[0]
capex_ratio = capex_past_year/net_revenues_past_year[0]
dep_amort_ratio = depreciation_and_amortization_past_year[0]/net_revenues_past_year[0]
first_ppe_forecast = ppe_past_two_years[1]+capex_ratio*forecast_revenues_base[0]-dep_amort_ratio*forecast_revenues_base[0]


cash_base_forecasted = np.zeros(number_of_years)
receivables_base_forecasted = np.zeros(number_of_years)
inventory_base_forecasted = np.zeros(number_of_years)
other_current_assets_base_forecasted = np.zeros(number_of_years)
ppe_base_forecasted = np.zeros(number_of_years)
intangible_assets_base_forecasted = np.zeros(number_of_years)
other_lt_assets_base_forecasted = np.zeros(number_of_years)
accounts_payable_base_forecasted = np.zeros(number_of_years)
income_taxes_payable_base_forecasted = np.zeros(number_of_years)
accrued_expenses_base_forecasted = np.zeros(number_of_years)
other_current_liabilities_base_forecasted = np.zeros(number_of_years)
lt_debt_base_forecasted = np.zeros(number_of_years)
other_lt_liabilities_base_forecasted = np.zeros(number_of_years)
pref_stock_base_forecasted = np.zeros(number_of_years)
common_stock_base_forecasted = np.zeros(number_of_years)
apic_base_forecasted = np.zeros(number_of_years)
re_base_forecasted = np.zeros(number_of_years)
treasury_stock_base_forecasted = np.zeros(number_of_years)
dividends_base_forecasted = np.zeros(number_of_years)
dep_amort_base_forecasted = np.zeros(number_of_years)
capex_base_forecasted = np.zeros(number_of_years)
total_assets_base_forecasted = np.zeros(number_of_years)
total_liabilities_base_forecasted = np.zeros(number_of_years)
total_equity_base_forecasted = np.zeros(number_of_years)

def balance_sheet_forecast(market_outlook, forecasted_revenues, forecasted_income, forecasted_cogs, forecasted_sga):
  if (market_outlook=="base"):
    for i in range(number_of_years):
      receivables_base_forecasted[i] = forecasted_revenues[i]/receivables_ratio
      inventory_base_forecasted[i] = forecasted_cogs[i]/inventory_ratio
      other_current_assets_base_forecasted[i] = forecasted_sga[i]/prepaid_expenses_ratio
   
      capex_base_forecasted[i] = capex_ratio*forecasted_revenues[i]
      dep_amort_base_forecasted[i] = dep_amort_ratio*forecasted_revenues[i]

      if i==0:
        ppe_base_forecasted[i] = first_ppe_forecast
      else:
        ppe_base_forecasted[i] = ppe_base_forecasted[i-1]+capex_base_forecasted[i]-dep_amort_base_forecasted[i]
      
      intangible_assets_base_forecasted[i] = intangible_assets_past_year[0]
      other_lt_assets_base_forecasted[i] = other_long_term_assets_past_year[0]

      accounts_payable_base_forecasted[i] = forecasted_cogs[i]/payables_ratio
      income_taxes_payable_base_forecasted[i] = income_taxes_payable_past_year[0]

      accrued_expenses_base_forecasted[i] = forecasted_sga[i]/accrued_expenses_ratio
      other_current_liabilities_base_forecasted[i] = other_current_liabilities_past_year[0]
      lt_debt_base_forecasted[i] = forecasted_revenues[i]/long_term_debt_ratio
      other_lt_liabilities_base_forecasted[i] = forecasted_revenues[i]/other_long_term_liabilities_ratio

      dividends_base_forecasted[i] = dividends_ratio * forecasted_income[i]
      pref_stock_base_forecasted[i] = preferred_stock_past_year[0]
      common_stock_base_forecasted[i] = common_stock_past_year[0]
      apic_base_forecasted[i] = apic_past_year[0]
      treasury_stock_base_forecasted[i] = treasury_stock_past_year[0]

      if i==0:
        re_base_forecasted[i] = retained_earnings_past_year[0] + forecasted_income[i] - dividends_base_forecasted[i]
      else:
        re_base_forecasted[i] = re_base_forecasted[i-1] + forecasted_income[i] - dividends_base_forecasted[i]

      total_liabilities_base_forecasted[i] = accounts_payable_base_forecasted[i] + income_taxes_payable_base_forecasted[i] + accrued_expenses_base_forecasted[i] + other_current_liabilities_base_forecasted[i] + lt_debt_base_forecasted[i] + other_lt_liabilities_base_forecasted[i]
      total_equity_base_forecasted[i] = pref_stock_base_forecasted[i] + common_stock_base_forecasted[i] + apic_base_forecasted[i] + re_base_forecasted[i] - treasury_stock_base_forecasted[i]

      cash_base_forecasted[i] = total_liabilities_base_forecasted[i] + total_equity_base_forecasted[i] - (receivables_base_forecasted[i]+inventory_base_forecasted[i]+other_current_assets_base_forecasted[i]+intangible_assets_base_forecasted[i]+ppe_base_forecasted[i]+other_lt_assets_base_forecasted[i])
      total_assets_base_forecasted[i] = cash_base_forecasted[i] + receivables_base_forecasted[i]+inventory_base_forecasted[i]+other_current_assets_base_forecasted[i]+intangible_assets_base_forecasted[i]+ppe_base_forecasted[i]+other_lt_assets_base_forecasted[i]

      if(total_assets_base_forecasted[i]-total_equity_base_forecasted[i]-total_liabilities_base_forecasted[i]<1e-5):
        continue
      else:
        print("Total assets do not equal total liabilities plus shareholder's equity.")


balance_sheet_forecast("base", forecast_revenues_base, forecast_net_income_base, cogs_forecasted_base, sga_forecasted_base)
