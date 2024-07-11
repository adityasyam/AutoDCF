from constants import number_of_years, tax_rate, cash_past_year, receivables_past_year, \
inventory_past_two_years, other_current_assets_past_year, ppe_past_two_years, intangible_assets_past_year, \
other_long_term_assets_past_year, accounts_payable_past_year, income_taxes_payable_past_year, \
accrued_expenses_past_year, other_current_liabilities_past_year, long_term_debt_past_year, \
other_long_term_liabilities_past_year, preferred_stock_past_year, common_stock_past_year, \
apic_past_year, retained_earnings_past_year, treasury_stock_past_year, net_revenues_past_year, \
COGS_past_year, SGA_past_year, dividends_past_year, net_income_past_year, depreciation_and_amortization_past_year

from income_statement import forecast_revenues_base, forecast_net_income_base

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



