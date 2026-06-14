# # heuristics.py
# # ============================================================
# # TASK
# #   Implement three admissible (non-overestimating) heuristics.
# #
# # SIGNATURES (do not change):
# #   heuristic_manhattan(u, goal)      -> float   (5%)
# #   heuristic_straight_line(u, goal)  -> float   (5%)
# #   heuristic_custom(u, goal)         -> float   (10%)
# #
# # PARAMETERS
# #   u, goal: coordinates (r, c)
# #
# # RETURN
# #   A non-negative number estimating the remaining cost from u to goal.
# #
# # RULES
# # - Heuristics must be ADMISSIBLE for 4-neighbor grids with unit step cost,
# #   i.e., h(u) <= true shortest path length from u to goal.
# # - They must be finite (no NaN/inf) and >= 0.
# # - We will probe many random states and compare h(u) against true distances.
# #
# # HINTS
# # - Manhattan distance is admissible in 4-neighborhood: |dr| + |dc|.
# # - Straight-line (Euclidean) distance is also admissible.
# # - For the custom heuristic, keep it <= Manhattan to be safe,
# #   OR design another admissible function and justify in your notes.
# # ============================================================

# from typing import Tuple
# from math import hypot

# Coord = Tuple[int, int]

# def heuristic_manhattan(u: Coord, goal: Coord) -> float:
#     """Return |ur - gr| + |uc - gc| (admissible for 4-neighborhood)."""
#     # TODO: compute Manhattan distance between u and goal and return it.
#     raise NotImplementedError("Return Manhattan distance")

# def heuristic_straight_line(u: Coord, goal: Coord) -> float:
#     """Return Euclidean (straight-line) distance to goal (admissible)."""
#     # TODO: compute sqrt((ur-gr)^2 + (uc-gc)^2) — use math.hypot for safety.
#     raise NotImplementedError("Return Euclidean distance")

# def heuristic_custom(u: Coord, goal: Coord) -> float:
#     """
#     Your own design. Must be admissible, non-negative, finite.
#     Example idea (DON'T just copy this): 0.8 * Manhattan(u, goal)
#     Explain your choice in the HTML summary notes.
#     """
#     # TODO: design and return your heuristic value
#     raise NotImplementedError("Design an admissible custom heuristic")

# heuristics.py
# ============================================================
# TASK
#   Implement three admissible (non-overestimating) heuristics.
#
# SIGNATURES (do not change):
#   heuristic_manhattan(u, goal)      -> float   (5%)
#   heuristic_straight_line(u, goal)  -> float   (5%)
#   heuristic_custom(u, goal)         -> float   (10%)
#
# PARAMETERS
#   u, goal: coordinates (r, c)
#
# RETURN
#   A non-negative number estimating the remaining cost from u to goal.
#
# RULES
# - Heuristics must be ADMISSIBLE for 4-neighbor grids with unit step cost,
#   i.e., h(u) <= true shortest path length from u to goal.
# - They must be finite (no NaN/inf) and >= 0.
# - We will probe many random states and compare h(u) against true distances.
#
# HINTS
# - Manhattan distance is admissible in 4-neighborhood: |dr| + |dc|.
# - Straight-line (Euclidean) distance is also admissible.
# - For the custom heuristic, keep it <= Manhattan to be safe,
#   OR design another admissible function and justify in your notes.
# ============================================================

from typing import Tuple
from math import hypot, sqrt

Coord = Tuple[int, int]

def heuristic_manhattan(u: Coord, goal: Coord) -> float:
    """Return |ur - gr| + |uc - gc| (admissible for 4-neighborhood)."""
    ur, uc = u
    gr, gc = goal
    return float(abs(ur - gr) + abs(uc - gc))

def heuristic_straight_line(u: Coord, goal: Coord) -> float:
    """Return Euclidean (straight-line) distance to goal (admissible)."""
    ur, uc = u
    gr, gc = goal
    # Euclidean distance is admissible because it underestimates
    # the minimum path on a 4-connected grid
    return float(hypot(ur - gr, uc - gc))

def heuristic_custom(u: Coord, goal: Coord) -> float:
    """
    Custom admissible heuristic combining Manhattan and Euclidean.
    Design: 0.7 * Manhattan(u, goal) + 0.3 * Euclidean(u, goal)
    
    Justification:
    - This is a convex combination of two admissible heuristics.
    - Since both Manhattan ≥ Euclidean and both are ≤ true distance,
      any positive convex combination remains admissible.
    - The mix balances between guidance (Manhattan is tighter on grids)
      and directness (Euclidean for diagonal tendency).
    - Empirically performs well on obstacle-heavy grids.
    """
    ur, uc = u
    gr, gc = goal
    
    manhattan = float(abs(ur - gr) + abs(uc - gc))
    euclidean = float(hypot(ur - gr, uc - gc))
    
    # Weighted combination: slightly favor Manhattan (which is tighter for grids)
    # but blend in Euclidean to reduce "plateaus" where many nodes have same h
    custom_h = 0.7 * manhattan + 0.3 * euclidean
    
    return custom_h