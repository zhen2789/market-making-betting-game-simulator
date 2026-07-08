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

# Step 4 - red_black_card_game_value (not yet solved)
# TODO: implement

# Step 5 - make_quotes (not yet solved)
# TODO: implement

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

