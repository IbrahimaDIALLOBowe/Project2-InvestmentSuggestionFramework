import numpy as np


class IndustryInfo:
    def __init__(self, has_dividend, use_dcf, use_cap_rate_market_model):
        self.has_dividend = has_dividend
        self.use_dcf = use_dcf
        self.use_cap_rate_market_model = use_cap_rate_market_model


class ValuationCalculator:


    def __init__(self, debug_level=0):
        self.__debug_level = 0
        # Source: https://www.valentiam.com/newsandinsights/ebitda-multiples-by-industry
        self.__industry_multiples = {
            "Healthcare information and technology": 24.81,
            "Airlines": 8.16,
            "Drugs, biotechnology": 13.29,
            "Hotels and casinos": 12.74,
            "Retail, general": 12.21,
            "Retail, food": 8.93,
            "Utilities, excluding water": 14.13,
            "Homebuilding": 10.95,
            "Medical equipment and supplies": 22.67,
            "Oil and gas, exploration and production": 4.89,
            "Telecom, equipment (phones & handheld devices)": 13.42,
            "Professional information services (big data)": 26.35,
            "Software, system & application": 24.00,
            "Wireless telecommunications services": 6.64
        }
        self.__industry_info = {
            "Technology": IndustryInfo(False, True, False)
        }


    def compute_value_list(self, stock_info_container):
        for analysis in stock_info_container.keys():
            for stock in
        return None


    def compute_value(self,
        industry
        ):
        if self.__industry_info[industry].has_dividend:
            return self.compute_value__dividend_discount_model()
        elif self.__industry_info[industry].use_dcf:
            return self.compute_value__dcf()
        elif self.__industry_info[industry].use_cap_rate_market_model:  # Need cap rate; prefer real estate industry
            return self.compute_value__cap_rate_market_model()
        else:
            return self.compute_value__relative_valuation_market_model()


    # --------------------------------------------------------------------------
    # Dividend Discount Model
    # --------------------------------------------------------------------------


    # TODO Correlate industries to changing dividends
    def compute_value__dividend_discount_model(self,
        ticker,
        #dividend_yield_fractional, # Dividend yield
        #npv, # Net present value
        #wacc, # Weighted cost of capital
        #eps, # Earnings per share
        #market_cap,
        r,  # Cost of equity capital == interest rate
        g  # Growth rate == eps growth
    ):
        dividend_next_year = np.nan
        npv = dividend_next_year / (r - g)
        return npv


    # --------------------------------------------------------------------------
    # Cap-M Model
    # --------------------------------------------------------------------------


    # Capitalization of earnings business valuation
    # Mostly for real estate
    def compute_value__cap_rate_market_model(self,
        industry_multiples,  # Dictionary of industry multiples
        market_cap,
        capitalization_rate  # net operating income / value
        ):
        npv = np.nan
        return npv / capitalization_rate


    # --------------------------------------------------------------------------
    # Market Relative Model
    # --------------------------------------------------------------------------
    
    def equity_value(
        market_value_of_equity,
        market_value_of_debt,
        cash
    ):
        return market_value_of_equity + market_value_of_debt - cash


    # Enterprise-Based Approach
    def compute_market_value(
        equity_value,
        expected_ebitda,
        ebitda
    ):
        return (equity_value)/(ebitda) * expected_ebitda


    # def compute_value__relative_valuation_market_model(self,
    #     industry,
    #     ebitda
    #     ):
    #     return ebitda * self.__industry_multiples[industry]

    
    # --------------------------------------------------------------------------
    # DCF Model
    # Assuming the dividend doesnt grow: price = (DIV_1)/(1+R) + (DIV_2)/(1+R)...
    # Assuming dividend is expected to grow: price = (DIV)/(R-g)
    # --------------------------------------------------------------------------
    

    def compute_cost_of_equity(
        risk_free_rate,
        market_rate_of_return,
        beta
    ):
        return risk_free_rate + beta * (market_rate_of_return - risk_free_rate)


    def compute_wacc(cost_of_equity):

        value_of_equity = np.nan
        equity = np.nan
        debt = np.nan
        cost_of_debt = np.nan
        corporate_tax_rate = np.nan

        wacc = (cost_of_equity) * ( (value_of_equity) / (equity + debt) )
        wacc += (debt / (equity + debt)) * cost_of_debt * (1 - corporate_tax_rate)
        return wacc


    # Discount cashflow model
    def compute_value__dcf(self,
        ebitda_projection,  # 5-year projection # TODO use a MA
        wacc,  # Discount rate r == wacc
        # cashflow_multiple,
        ):
        
        year_count = len(ebitda_projection)
        npv = 0
        for y in range(0, year_count):
            ebitda = ebitda_projection[y]
            npv += ebitda / (1 + wacc) ** (y+1)
        
        return npv
