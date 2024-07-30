from constants import number_of_years, tax_rate, receivables_past_year, inventory_past_two_years, \
other_current_assets_past_year, ppe_past_two_years, intangible_assets_past_year, cash_past_year, \
accrued_expenses_past_year, other_current_liabilities_past_year, long_term_debt_past_year, \
other_long_term_liabilities_past_year, preferred_stock_past_year, common_stock_past_year, \
apic_past_year, retained_earnings_past_year, treasury_stock_past_year, net_revenues_past_year, \
COGS_past_year, SGA_past_year, dividends_past_year, net_income_past_year, depreciation_and_amortization_past_year, \
accounts_payable_past_year, income_taxes_payable_past_year

from income_statement import forecast_net_income_base

from balance_sheet import dep_amort_base_forecasted, receivables_base_forecasted, inventory_base_forecasted, \
other_current_assets_base_forecasted, intangible_assets_base_forecasted, other_lt_assets_base_forecasted, \
accounts_payable_base_forecasted, income_taxes_payable_base_forecasted, accrued_expenses_base_forecasted, \
other_current_liabilities_base_forecasted, lt_debt_base_forecasted, other_lt_liabilities_base_forecasted, \
capex_base_forecasted, dividends_base_forecasted

import numpy as np

change_receivables_base = np.zeros(number_of_years)
change_inventories_base = np.zeros(number_of_years)
change_oca_base = np.zeros(number_of_years)
change_intangible_assets_base = np.zeros(number_of_years)
change_payables_base = np.zeros(number_of_years)
change_taxes_payables_base = np.zeros(number_of_years)
change_accrued_expenses_base = np.zeros(number_of_years)
change_ocl_base = np.zeros(number_of_years)
change_olt_liabilities_base = np.zeros(number_of_years)
cash_flow_operations_base = np.zeros(number_of_years)

capex_base = np.zeros(number_of_years)
change_otl_assets_base = np.zeros(number_of_years)
cash_flow_investments_base = np.zeros(number_of_years)

change_long_term_debt_base = np.zeros(number_of_years)
net_equity_payout = np.zeros(number_of_years)
cash_flow_financing_base = np.zeros(number_of_years)

change_in_cash_base = np.zeros(number_of_years)

def cash_flow_forecast(market_outlook):

  if market_outlook=="base":

    for i in range(number_of_years):
      if i==0:
        change_receivables_base[i] = receivables_past_year[0]-receivables_base_forecasted[i]
        change_inventories_base[i] = inventory_past_two_years[1]-inventory_base_forecasted[i]
        change_oca_base[i] = other_current_assets_past_year[0]-other_current_assets_base_forecasted[i]
        change_intangible_assets_base[i] = intangible_assets_past_year[0]-intangible_assets_base_forecasted[i]

        change_payables_base[i] = accounts_payable_base_forecasted[i] - accounts_payable_past_year[0]
        change_taxes_payables_base[i] = income_taxes_payable_base_forecasted[i] - income_taxes_payable_past_year[0]
        change_accrued_expenses_base[i] = accrued_expenses_base_forecasted[i] - accrued_expenses_past_year[0]
        change_ocl_base[i] = other_current_liabilities_base_forecasted[i] - other_current_liabilities_past_year[0]
        change_olt_liabilities_base[i] = other_lt_liabilities_base_forecasted[i] - other_long_term_liabilities_past_year[0]

      else:
        change_receivables_base[i] = receivables_base_forecasted[i-1]-receivables_base_forecasted[i]
        change_inventories_base[i] = inventory_base_forecasted[i-1]-inventory_base_forecasted[i]
        change_oca_base[i] = other_current_assets_base_forecasted[i-1]-other_current_assets_base_forecasted[i]
        change_intangible_assets_base[i] = intangible_assets_base_forecasted[i-1]-intangible_assets_base_forecasted[i]

        change_payables_base[i] = accounts_payable_base_forecasted[i] - accounts_payable_base_forecasted[i-1]
        change_taxes_payables_base[i] = income_taxes_payable_base_forecasted[i] - income_taxes_payable_base_forecasted[i-1]
        change_accrued_expenses_base[i] = accrued_expenses_base_forecasted[i] - accrued_expenses_base_forecasted[i-1]
        change_ocl_base[i] = other_current_liabilities_base_forecasted[i] - other_current_liabilities_base_forecasted[i-1]
        change_olt_liabilities_base[i] = other_lt_liabilities_base_forecasted[i] - other_lt_liabilities_base_forecasted[i-1]

      cash_flow_operations_base[i] = change_receivables_base[i]+change_inventories_base[i]+change_oca_base[i]+change_intangible_assets_base[i]+change_payables_base[i]+change_taxes_payables_base[i]+change_accrued_expenses_base[i]+change_ocl_base[i]+change_olt_liabilities_base[i]


cash_flow_forecast("base")
