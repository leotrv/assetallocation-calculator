#define variables
token = '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'
yield_stocks = 5.2
yield_bonds = 0.8


def get_variables():
    while True:
        expected_yield = input('Please enter the expected yield [%]: ')
        if expected_yield.isdigit() or expected_yield.isdecimal():
            expected_yield = float(expected_yield)
            break
        else: print("You must enter a number in range 1-100!")

    while True:
        risk_bearing_capacity = input('Please enter your risk-bearing capacity (1-10): ') #TODO: find method to calculate/find out risk-bearing capacity
        if risk_bearing_capacity.isdigit():
            risk_bearing_capacity = int(risk_bearing_capacity)
            break
        else: print("You must enter a number in range 1-10!")

    while True:
        liquidity_needs = input('Please enter the expected liquidity needs [€]: ')
        if liquidity_needs.isdigit():
            liquidity_needs = int(liquidity_needs)
            break
        else: print("You must enter a number in range 0-50000")

    while True:
        investment_horizon = input('Please enter the expected investment horizon [years]: ')
        if investment_horizon.isdigit():
            investment_horizon = int(investment_horizon)
            break
        else: print("You must enter a number in range 1-50!")

    return expected_yield, risk_bearing_capacity, liquidity_needs, investment_horizon


def lvl1_asset_allocation(expected_yield, risk_bearing_capacity, liquidity_needs, investment_horizon, yield_stocks, yield_bonds):
    if expected_yield > yield_bonds:
        if expected_yield <= yield_stocks:
            allocation_stocks = expected_yield / (yield_stocks + yield_bonds) #not exactly accurate yet - exact formula has to be found out yet
        else:
            allocation_stocks = 100 
            print('Expected yield too high, selected yield of stocks as its the highest on this asset')
    else:
        allocation_stocks = 0
    
    
    allocation_bonds = 100 - allocation_stocks
    return allocation_stocks, allocation_bonds

def main():
    variables = get_variables()
    allocation = lvl1_asset_allocation(variables[0],variables[1],variables[2],variables[3], yield_stocks, yield_bonds)

    print('Allocation: ', allocation)
    return variables


main()