import threading
threading.stack_size(67108864)

# initilization
def initialize(context):
    context.stocks = symbols('AAPL', 'SPY', 'GOOG')
    context.nshares = 100
    context.has_ordered = False
    
    # Rebalance every day, 1 hour after market open.
    schedule_function(rebalance, date_rules.every_day(), time_rules.market_open(hours=1))
    
    # Record tracking variables at the end of each day.
    schedule_function(record_vars, date_rules.every_day(), time_rules.market_close())
    
# rebalance
def rebalance(context, data):
    # Compute allocations
    long_stocks = context.stocks
    if context.has_ordered:
        long_stocks = long_stocks[1:]
    allocations = compute_allocations(long_stocks, context.nshares)
    
    # Rebalance
