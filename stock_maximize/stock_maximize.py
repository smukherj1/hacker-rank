import sys

def process_test_case():
    num_days = int(sys.stdin.readline().strip())
    share_prices = [int(i) for i in sys.stdin.readline().strip().split()]
    assert(num_days == len(share_prices))
    next_max = [-1]
    cur_max = share_prices[-1]
    for i in range(len(share_prices) - 2, -1, -1):
        if share_prices[i] <= cur_max:
            next_max.append(cur_max)
        else:
            next_max.append(-1)
            cur_max = share_prices[i]
    next_max.reverse()
    revenue = 0
    num_units = 0
    for i in range(len(share_prices)):
        if next_max[i] > share_prices[i]:
            revenue -= share_prices[i]
            num_units += 1
            #print 'Buy 1 @ %d because next max is %d. Total earnings: %d with %d shares in hand'%(share_prices[i], next_max[i], revenue, num_units)
        else:
            revenue += num_units * share_prices[i]
            #print 'Sell %d @ %d because next max is %d. Total earnings: %d'%(num_units, share_prices[i], next_max[i], revenue)
            num_units = 0
    print revenue
    return

num_test_cases = int(sys.stdin.readline().strip())
for i in range(num_test_cases):
    process_test_case()