"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    # TODO: return the expected value of the discrete distribution (values, probabilities).
    return float(np.sum(np.asarray(values) * np.asarray(probabilities)))
    pass

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    # TODO: return {'value': expected winnings under optimal reroll policy, 'reroll_faces': sorted faces to reroll}
    faces = np.arange(1, sides+1)
    mu = expected_value(faces, [1/sides]*sides)
    expected_payouts = np.maximum(faces, mu)
    value = expected_value(expected_payouts, [1/sides]*sides)
    reroll_faces = np.arange(1, mu).astype(int).tolist()
    return {'value': value, 'reroll_faces': reroll_faces}
    pass

# Step 3 - pay_per_reroll_die_game
def pay_per_reroll_die_game(sides, reroll_cost):
    # TODO: return {'threshold': t, 'value': V} for the pay-per-reroll die game under the optimal threshold policy.
    V_star = float('-inf')
    t_star = 0
    for t in range(1, sides+1):
        V = (t+sides)/2 - (t-1)/(sides - t + 1) * reroll_cost
        if V > V_star:
            V_star = V
            t_star = t
    return {'threshold': t_star, 'value': V_star}
    pass

# Step 4 - red_black_card_game_value
import functools
from functools import lru_cache

@lru_cache(maxsize=None)
def V(r, b):
    if r == 0 and b == 0: # red and black run out
        return 0.0
    if r == 0: # red runs out, no gain so we stop
        return 0.0
    if b == 0:
        return float(r) # draw all red cards since black is out
    cont = ((r / (r + b)) * (1.0 + V(r - 1, b)) + 
            (b / (r + b)) * (-1.0 + V(r, b - 1)))
    return max(0.0, cont)

def red_black_card_game_value(num_red, num_black):
    if num_red == 0:
        return {'value': 0.0, 'stop_now': True} # edge case: if empty deck or all black, stop
    if num_black == 0:
        return {'value': float(num_red), 'stop_now': False} # edge case: if all red, return num_red
    # TODO: return {'value': expected payout under optimal stopping, 'stop_now': whether to stop immediately}.
    cont = ((num_red / (num_red + num_black)) * (1.0 + V(num_red - 1, num_black)) + 
            (num_black / (num_red + num_black)) * (-1.0 + V(num_red, num_black - 1)))
    value = max(0.0, cont)
    stop_now = (cont <= 0.0)
    return {'value': value, 'stop_now': stop_now}
    pass

# Step 5 - make_quotes
def make_quotes(fair_value, spread_width):
    # TODO: return a dict with 'bid' and 'ask' symmetric around fair_value with total width spread_width
    half = spread_width / 2
    bid = fair_value - half
    ask = fair_value + half
    return {'bid': bid, 'ask': ask}
    pass

# Step 6 - execute_trade
def execute_trade(state, side, bid, ask, size=1):
    # TODO: apply a counterparty trade against your bid/ask and return updated state
    new_cash = state['cash']
    new_inv = state['inventory']
    if side == 'buy':
        new_cash += size * ask
        new_inv -= size
        #company buys from us at our ask, NOTE: OUR cash and inventory
    if side == 'sell':
        new_cash -= size * bid
        new_inv += size
        #company sells to us at our bid
    return {'cash': new_cash, 'inventory': new_inv}
    pass

# Step 7 - mark_to_market_pnl
def mark_to_market_pnl(cash, inventory, settlement_value):
    # TODO: return total P&L given cash, remaining inventory, and settlement value.
    return cash + inventory * settlement_value
    pass

# Step 8 - adverse_selection_loss
import numpy as np

def adverse_selection_loss(fair_value, bid, ask, informed_values, informed_probabilities):
    # TODO: expected loss = E[(v-ask)*1{v>ask}] + E[(bid-v)*1{v<bid}] over informed_values.
    values = np.asarray(informed_values, dtype=float)
    probs = np.asarray(informed_probabilities, dtype=float)
    loss = np.maximum(values - ask, 0.0) + np.maximum(bid - values, 0.0)
    total = np.sum(loss * probs)
    return float(total)
    pass

# Step 9 - uncertainty_spread
def uncertainty_spread(base_spread, uncertainty):
    """Return a spread width >= base_spread that grows with uncertainty."""
    # TODO: choose a spread width that is at least base_spread and increases with uncertainty.
    k = 0.1
    return base_spread + k * uncertainty
    pass

# Step 10 - inventory_skewed_quotes
def inventory_skewed_quotes(fair_value, spread_width, inventory, skew_strength):
    # TODO: return {'bid', 'ask'} shifted against inventory around fair_value
    half = spread_width / 2
    shift = skew_strength * inventory
    mid_prime = fair_value - shift
    return {'bid': mid_prime - half, 'ask': mid_prime + half}
    pass

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

