import math

#define variables
yield_stocks = 5.2
yield_bonds = 0.8

def get_saving_rate():
    while True:
        saving_rate = input('Please enter your saving rate [€]: ')
        if saving_rate.isdigit():
            saving_rate = int(saving_rate)
            break
        elif saving_rate.replace('.','',1).isdigit():
            saving_rate = float(saving_rate)
            break
        else: print('Please enter a number!')
    return saving_rate

def get_expected_yield():
    while True:
        expected_yield = input('Please enter the expected yield [%]: ')
        if expected_yield.isdigit():
            expected_yield = int(expected_yield)
            break
        elif expected_yield.replace('.','',1).isdigit():
            expected_yield = float(expected_yield)
            break
        else: print("You must enter a number in range 1-100!")
    return expected_yield


def get_risk_bearing_capacity():
    while True:
        risk_bearing_capacity = input('Please enter your risk-bearing capacity (1-10): ') #TODO: find method to calculate/find out risk-bearing capacity
        if risk_bearing_capacity.isdigit():
            risk_bearing_capacity = int(risk_bearing_capacity)
            break
        else: print("You must enter a number in range 1-10!")
    return risk_bearing_capacity


def get_liquidity_needs():
    while True:
        liquidity_needs = input('Please enter the expected liquidity needs [€]: ')
        if liquidity_needs.isdigit():
            liquidity_needs = int(liquidity_needs)
            break
        else: print("You must enter a number in range 0-50000")
    return liquidity_needs


def get_investment_horizon():
    while True:
        investment_horizon = input('Please enter the expected investment horizon [years]: ')
        if investment_horizon.isdigit():
            investment_horizon = int(investment_horizon)
            break
        else: print("You must enter a number in range 1-50!")
    return investment_horizon


def lvl1_asset_allocation(saving_rate, expected_yield, risk_bearing_capacity, liquidity_needs, investment_horizon, yield_stocks, yield_bonds):
    #use expected_yield to calculate asset allocation
    if expected_yield > yield_bonds:
        if expected_yield < yield_stocks:
            quotient_bonds = ((1+yield_bonds/100)-(1+yield_stocks/100))/((1+expected_yield/100)-(1+yield_stocks/100))
            quotient_stocks = 1/(1-1/quotient_bonds)
            allocation_stocks = 100/quotient_stocks
            allocation_bonds = 100/quotient_bonds
        else:
            allocation_stocks = 100
            allocation_bonds = 0
            print('Expected yield too high, selected 100 % stocks to get nearest to preferred yield...')
    else:
        allocation_stocks = 0
        allocation_bonds = 100

    amount_stocks = allocation_stocks / 100 * saving_rate
    amount_bonds = allocation_bonds / 100 * saving_rate

    #use risk_bearing_capacity (1-10) to recalculate asset allocation - 5 means allocation remains the same, 10 doubles stocks allocation, 0 set stocks allocation to 0
    allocation_stocks_riskadjusted = allocation_stocks * 2 * risk_bearing_capacity / 10
    if allocation_stocks > allocation_stocks_riskadjusted:
        allocation_stocks = allocation_stocks_riskadjusted
    allocation_bonds = 100 - allocation_stocks

    #use liquidity_needs [€] to recalculate asset allocation
    no_investment_months = math.ceil(liquidity_needs/saving_rate)

    #use investment_horizon [years] to recalculate asset allocation
    final_amount_stocks = saving_rate * allocation_stocks/100 *investment_horizon * 12 - no_investment_months * saving_rate * allocation_stocks/100
    final_amount_bonds = saving_rate * allocation_bonds/100 * investment_horizon * 12 - no_investment_months * saving_rate * allocation_bonds/100
    if investment_horizon < no_investment_months/12:
        final_amount_stocks = 0
        final_amount_bonds = 0
    return allocation_stocks, amount_stocks, allocation_bonds, amount_bonds, no_investment_months, final_amount_stocks, final_amount_bonds

def main():
    saving_rate = get_saving_rate()
    expected_yield = get_expected_yield()
    risk_bearing_capacity = get_risk_bearing_capacity()
    liquidity_needs = get_liquidity_needs()
    investment_horizon = get_investment_horizon()
    allocation = lvl1_asset_allocation(saving_rate, expected_yield, risk_bearing_capacity, liquidity_needs, investment_horizon, yield_stocks, yield_bonds)

    # print(f'Months without investment to meet your liquidity targets: {math.ceil(allocation[4])}')
    # print(f'Suggested allocation:  {round(allocation[0],2)}% stocks: {round(allocation[1],2)} €/month, {round(allocation[2],2)}% bonds: {round(allocation[3],2)} €/month')
    # print(f'At the end of your investment horizon you will have invested {round(allocation[5])}€ in stocks and {round(allocation[6])}€ in bonds.')

    monthly_distribution_dict = {'months_without_investment': round(allocation[4],2) ,'amount_stocks_in_euro': round(allocation[1],2), 'amount_bonds_in_euro': round(allocation[3],2)}
    final_distribution_dict = {'liquidity_in_euro': saving_rate * allocation[4], 'stocks_in_euro': round(allocation[5],2), 'bonds_in_euro': round(allocation[6],2)}

    print(monthly_distribution_dict)
    print(final_distribution_dict)

main()