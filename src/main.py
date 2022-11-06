#define variables
yield_stocks = 5.2
yield_bonds = 0.8


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


def lvl1_asset_allocation(expected_yield, risk_bearing_capacity, liquidity_needs, investment_horizon, yield_stocks, yield_bonds):
    #use expected_yield to calculate asset allocation
    if expected_yield > yield_bonds:
        if expected_yield < yield_stocks:
            quotient_bonds = ((1+yield_bonds/100)-(1+yield_stocks/100))/((1+expected_yield/100)-(1+yield_stocks/100))
            quotient_stocks = 1/(1-1/quotient_bonds)
            allocation_stocks = round(100/quotient_stocks, 2)
            allocation_bonds = round(100/quotient_bonds, 2)
        else:
            allocation_stocks = 100
            allocation_bonds = 0
            print('Expected yield too high, selected 100 % stocks to get nearest to preferred yield')
    else:
        allocation_stocks = 0
        allocation_bonds = 100

    #use risk_bearing_capacity (1-10) to recalculate asset allocation - 5 means allocation remains the same, 10 doubles stocks allocation, 0 set stocks allocation to 0
    allocation_stocks = allocation_stocks * 2 * risk_bearing_capacity / 10
    if allocation_stocks > 100:
        allocation_stocks = 100
    allocation_bonds = 100 - allocation_stocks

    #use liquidity_needs [€] to recalculate asset allocation
    

    return allocation_stocks, allocation_bonds

def main():
    expected_yield = get_expected_yield()
    risk_bearing_capacity = get_risk_bearing_capacity()
    liquidity_needs = get_liquidity_needs()
    investment_horizon = get_investment_horizon()
    allocation = lvl1_asset_allocation(expected_yield, risk_bearing_capacity, liquidity_needs, investment_horizon, yield_stocks, yield_bonds)

    print(f'Suggested allocation:  {allocation[0]}% stocks, {allocation[1]}% bonds')


main()