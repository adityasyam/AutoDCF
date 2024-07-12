from constants import number_of_years, tax_rate, receivables_past_year, inventory_past_two_years, \
other_current_assets_past_year, ppe_past_two_years, intangible_assets_past_year, cash_past_year, \
accrued_expenses_past_year, other_current_liabilities_past_year, long_term_debt_past_year, \
other_long_term_liabilities_past_year, preferred_stock_past_year, common_stock_past_year, \
apic_past_year, retained_earnings_past_year, treasury_stock_past_year, net_revenues_past_year, \
COGS_past_year, SGA_past_year, dividends_past_year, net_income_past_year, depreciation_and_amortization_past_year

from income_statement import forecast_net_income_base

from balance_sheet import dep_amort_base_forecasted, receivables_base_forecasted, inventory_base_forecasted, \
other_current_assets_base_forecasted, intangible_assets_base_forecasted, other_lt_assets_base_forecasted, \
accounts_payable_base_forecasted, income_taxes_payable_base_forecasted, accrued_expenses_base_forecasted, \
other_current_liabilities_base_forecasted, lt_debt_base_forecasted, other_lt_liabilities_base_forecasted, \
capex_base_forecasted, dividends_base_forecasted

import numpy as np
