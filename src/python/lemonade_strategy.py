import math

def expected_profit(glasses, signs, price, cost, r1=1, p_storm=0):
    n1 = 54 - 2.4 * price if price < 10 else 3000 / (price * price)
    demand = min(int(r1 * n1 * (2 - math.exp(-0.5 * signs))), glasses)
    revenue = demand * price
    expense = glasses * cost + signs * 15
    return ((1 - p_storm) * revenue - expense, revenue - expense,
            glasses, signs, price)
    
while True:
    print('=============================================')
    print('Lemonsville weather report:')
    print('       0 = sunny')
    print('  30..70 = cloudy (% chance of rain)')
    print('      90 = road work')
    print('    -100 = hot and dry')
    print()
    weather = int(input('Enter weather report: '))
    cost = int(input('Enter cost per glass (cents): '))
    assets = int(input('Enter assets (cents): '))
    print()
    r1 = 1 - weather / 100
    p_storm = 0.25 if (30 <= weather <= 70) else 0
    e_profit, profit, glasses, signs, price = max(
        expected_profit(glasses, signs, price, cost, r1, p_storm)
        for glasses in range(min(1000, assets // cost) + 1)
        for signs in range(min(50, (assets - cost * glasses) // 15) + 1)
        for price in range(101))
    print(f'Make {glasses} glasses of lemonade.')
    print(f'Make {signs} advertising signs.')
    print(f'Charge {price} cents per glass.')
    print(f'Expected profit = ${e_profit/100:.2f}')
    if p_storm > 0:
        print(f'                 (${profit/100:.2f} with no thunderstorm)')
