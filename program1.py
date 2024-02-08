import sys

'''
    Finds the minimum number of dollars and each type of coin to represent a given amount of money
    Args: The amount of money in the format $X.YZ
    Returns: The minimum number of dollars and each type of coin
'''
args = sys.argv[1:] # get command line arguments

# process arguments: there must be exactly one of the format $X.YZ where 0 <= x <= 100
if len(args) > 1 or len(args) == 0:
    print("There must be exactly one argument, the dollar amount to analyze")
    sys.exit(-1)

amount = args[0]

if amount[0] != '$':
    print("The string must begin with a $")
    sys.exit(-1)

amount = amount[1:]

try:
    dollars, cents = amount.split('.', 1)
except:
    print("The string should include both dollars and cents")
    sys.exit(-1)

if len(dollars) < 1:
    print("The string must include a dollar amount")
    sys.exit(-1)
if len(cents) != 2:
    print("The number of cents should be a 2-digit integer between 00 and 99")
    sys.exit(-1)
    
try:
    dollars = int(dollars)
except:
    print("The dollar amount must be an integer")
    sys.exit(-1)

try:
    cents = int(cents)
except:
    print("The cent amount must be an integer")
    sys.exit(-1)

if not 0 <= dollars <= 100:
    print("The dollar amount must be between 0 and 100, inclusive")
    sys.exit(-1)


total_cents = 100*dollars + cents
coin_values = [100, 25, 10, 5, 1]
coin_names = ["dollars", "quarters", "dimes", "nickels", "pennies"]
coin_names_singular = ["dollar", "quarter", "dime", "nickel", "penny"]


# print out the minimum number of each coin
for i in range(len(coin_values)):
    num_of_coin = total_cents // coin_values[i]
    total_cents -= num_of_coin * coin_values[i]
    if num_of_coin > 0:
        print(f'{num_of_coin} {coin_names[i] if num_of_coin > 1 else coin_names_singular[i]}')