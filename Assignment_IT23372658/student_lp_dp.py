# student_lp_dp.py
from __future__ import annotations
from typing import List, Tuple, Optional
from functools import lru_cache
import math

"""
===========================================================
Overall Pseudocode & Study Guide (LP + DP)
===========================================================

A) Linear Programming in 2 variables (vertex enumeration)
   Goal: maximize Z = c1*x + c2*y subject to a1*x + a2*y <= b (and x>=0, y>=0)

   1) Model the feasible region:
      - Collect all given constraints (<= type).
      - Add non-negativity constraints: x>=0, y>=0.

   2) Enumerate candidate vertices:
      - Intersect every pair of constraint boundary lines (treat each as equality).
      - Keep only well-defined intersections (ignore parallel lines).
      - (Optionally) include the origin explicitly.

   3) Feasibility test:
      - For each candidate (x,y), check all constraints (<= type) with a small numeric tolerance.

   4) Objective evaluation:
      - Evaluate Z at each feasible vertex.
      - Select the best according to Z; tie-break deterministically if needed.

B) 0/1 Knapsack (Dynamic Programming)
   Problem: given values[i], weights[i], capacity C, pick subset to maximize total value without
            exceeding C.

   1) Bottom-Up Table (iterative):
      - Define dp[i][cap] = best value using items from i..n-1 with remaining capacity 'cap'.
      - Fill the table in an order that ensures subproblems are ready (e.g., i from n-1→0).
      - Transition: choose between skipping item i or taking it (if it fits), then record the best.

   2) Top-Down with Memoization (recursive):
      - Define f(i, cap): best value using items from i..n-1 with capacity 'cap'.
      - Base cases: end of items or cap==0 -> return 0.
      - Transition: if item i doesn't fit, skip; else max(skip, take).
      - Cache results to avoid recomputation.

Notes:
- Use a small tolerance EPS for LP comparisons with floats.
- Keep implementations simple, readable, and consistent with the above plan.
"""

# ---------- LP (12.5% of total grade) ----------
Constraint = Tuple[float, float, float]  # a1, a2, b  meaning  a1*x + a2*y <= b
EPS = 1e-9

def _intersect(c1: Constraint, c2: Constraint) -> Optional[Tuple[float, float]]:
    """
    Compute the intersection point of two *boundary lines* obtained from constraints.
    Each constraint (a1, a2, b) corresponds to a boundary line a1*x + a2*y = b.

    Solve the 2x2 linear system:
      a1*x + a2*y = b
      c1*x + c2*y = d
    """
    a1, a2, b = c1
    c1_coef, c2_coef, d = c2
    
    det = a1 * c2_coef - a2 * c1_coef
    
    if abs(det) < EPS:
        return None
    
    x = (b * c2_coef - a2 * d) / det
    y = (a1 * d - b * c1_coef) / det
    
    return (x, y)


def _is_feasible(pt: Tuple[float, float], constraints: List[Constraint]) -> bool:
    """
    Check whether point (x,y) satisfies ALL constraints a1*x + a2*y <= b (with tolerance).
    """
    x, y = pt
    for a1, a2, b in constraints:
        lhs = a1 * x + a2 * y
        if lhs > b + EPS:
            return False
    return True


def feasible_vertices(constraints: List[Constraint]) -> List[Tuple[float, float]]:
    """
    Enumerate and return all *feasible* vertices (x,y) of the polygonal feasible region.
    """
    all_constraints = list(constraints)
    
    # Add non-negativity constraints: x >= 0 and y >= 0
    # Represent as: -1*x + 0*y <= 0 (equivalently x >= 0)
    #               0*x + -1*y <= 0 (equivalently y >= 0)
    all_constraints.append((-1.0, 0.0, 0.0))  # x >= 0
    all_constraints.append((0.0, -1.0, 0.0))  # y >= 0
    
    candidates: List[Tuple[float, float]] = []
    
    n = len(all_constraints)
    for i in range(n):
        for j in range(i+1, n):
            intersection = _intersect(all_constraints[i], all_constraints[j])
            if intersection is not None:
                candidates.append(intersection)
    
    candidates.append((0.0, 0.0))
    
    feasible = []
    for pt in candidates:
        if _is_feasible(pt, all_constraints):
            feasible.append(pt)
    
    unique_feasible = []
    seen = set()
    for pt in feasible:
        rounded = (round(pt[0], 8), round(pt[1], 8))
        if rounded not in seen:
            seen.add(rounded)
            unique_feasible.append(pt)
    
    return unique_feasible


def maximize_objective(vertices: List[Tuple[float, float]], c1: float, c2: float) -> Tuple[Tuple[float, float], float]:
    """
    Evaluate Z = c1*x + c2*y over feasible vertices and return (best_point, best_value).
    """
    if not vertices:
        return ((0.0, 0.0), 0.0)
    
    best_point = vertices[0]
    best_value = c1 * vertices[0][0] + c2 * vertices[0][1]
    
    for pt in vertices[1:]:
        z = c1 * pt[0] + c2 * pt[1]
        
        if z > best_value + EPS:
            best_point = pt
            best_value = z
        elif abs(z - best_value) <= EPS:
            if pt[0] > best_point[0] + EPS or \
               (abs(pt[0] - best_point[0]) <= EPS and pt[1] > best_point[1] + EPS):
                best_point = pt
                best_value = z
    
    return (best_point, float(best_value))


# ---------- DP (12.5% of total grade) ----------
def knapsack_bottom_up(values: List[int], weights: List[int], capacity: int) -> int:
    """
    Bottom-up 0/1 knapsack. Return the optimal value (int).
    
    Table design:
      dp[i][cap] = best value using items i..n-1 with remaining capacity 'cap'.
      Dimensions: (n+1) x (capacity+1), initialized to 0.
      Fill order: i from n-1 down to 0; cap from 0 to capacity.
    """
    n = len(values)
    
    if n == 0 or capacity < 0:
        return 0
    if len(weights) != n:
        return 0
    

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    

    for i in range(n - 1, -1, -1):
        for cap in range(capacity + 1):
            skip = dp[i + 1][cap]
            
            take = 0
            if weights[i] <= cap:
                take = values[i] + dp[i + 1][cap - weights[i]]
            
            dp[i][cap] = max(skip, take)
    
    return dp[0][capacity]


def knapsack_top_down(values: List[int], weights: List[int], capacity: int) -> int:
    """
    Top-down (memoized) 0/1 knapsack. Return optimal value (int).

    Recurrence:
      f(i, cap) = 0                                     if i==n or cap==0
      f(i, cap) = f(i+1, cap)                           if weights[i] > cap
      f(i, cap) = max(
                      f(i+1, cap),                      # skip item i
                      values[i] + f(i+1, cap - w[i])    # take item i
                   )                                    otherwise
    """
    n = len(values)
    if n == 0 or capacity < 0:
        return 0
    if len(weights) != n:
        return 0

    @lru_cache(maxsize=None)
    def f(i: int, cap: int) -> int:
        if i == n or cap == 0:
            return 0
        
        if weights[i] > cap:
            return f(i + 1, cap)
        
        skip = f(i + 1, cap)
        take = values[i] + f(i + 1, cap - weights[i])
        
        return max(skip, take)

    return f(0, capacity)


# ------------- Optional local smoke test -------------
if __name__ == "__main__":
    # Minimal checks that won't reveal answers; just ensures your functions run.
    cons = [
        (1.0, 1.0, 6.0),
        (1.0, 0.0, 4.0),
        (0.0, 1.0, 5.0),
        (2.0, 1.0, 8.0),
    ]
    try:
        V = feasible_vertices(cons)
        print(f"[LP] #vertices found: {len(V)}")
        if V:
            bp, bv = maximize_objective(V, 3.0, 5.0)
            print(f"[LP] best vertex (masked): {bp}, value={bv:.2f}")
    except NotImplementedError:
        print("[LP] TODOs not yet implemented")

    vals = [6,5,18,15,10]
    wts  = [2,2,6,5,4]
    cap  = 10
    try:
        print("[DP] bottom-up (masked run):", knapsack_bottom_up(vals, wts, cap))
    except NotImplementedError:
        print("[DP] bottom-up TODO not implemented")
    try:
        print("[DP] top-down  (masked run):", knapsack_top_down(vals, wts, cap))
    except NotImplementedError:
        print("[DP] top-down  TODO not implemented")
        