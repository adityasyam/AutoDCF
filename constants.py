"""
TO BE MODIFIED AS REQUIRED BY USER.

This file contains all the constants used in the free cash flows valuation. 
Edit the constants below as required to suit you specific requirements and the 
code base will adapt automatically to give you your output. Our model relies on 
a complete forecasting of the income statement, the balance sheet, as well as
the statement of cash flows, resulting in forecasting free cash flows to firm 
for the number of years specified by the user. The line items are only taken for 
the past two years at most to simplify the number of inputs required of the user.
"""

#INTRINSIC NUMBERS USED FOR DISCOUNTED CASH FLOW VALUATION 

number_of_years = 5
"""
this is the number of years for which we forecast the statements, beyond which
the terminal value is used
"""

risk_free_rate = 4.50
"""
this is the risk free rate, usually determined by the rate of return on a 
10-year US Treasury bond
"""

industry_beta = 1.17 
"""
this is the industry beta of the given company you want to evaluate; to find
industry beta values for your industry, check the database at:
https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html
"""

market_risk_premium = 4.60
"""
this is the market risk premium, expressed in %
"""

tax_rate = 22.7
"""
this is the effective tax rate for the company being evaluated, expressed in %
"""

cost_of_debt = 8.0
"""
this is the cost of borrowing for the company, expressed in %
"""

terminal_growth_rate = 2.0 
"""
this is the terminal growth rate, expressed in %
"""

#INCOME STATEMENT ITEMS FOR PAST YEARS - PLEASE ENTER ALL MONETARY DATA IN A
#UNIFORM UNIT, FOR EG. ALL IN THOUSANDS OR ALL IN MILLIONS. ENTER IN THE FORM
#[year_t-1].

net_revenues_past_year = [3490.70]
"""
this list holds the company's net revenues for the previous fiscal year
"""

net_revenue_forecasted_growth_rates = [-19.36, 14.72, 14.72, 7.36, 4.03]
"""
this list holds the revenue growth rates for the next n years. the size of the
list is `number_of_years`
"""

COGS_past_year = [2904.60]
"""
this list contains the cost of goods sold for the previous fiscal year
"""

SGA_past_year = [267.70]
"""
this list contains the selling, general, and administrative expenses for the 
previous fiscal year
"""

amortization_past_year = [17.70]
"""
this list contains the amortization for the previous fiscal year
"""

interest_expense_past_year = [-20.50]
"""
this list contains the interest expense for the previous fiscal year
"""









