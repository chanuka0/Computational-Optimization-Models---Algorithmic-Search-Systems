# student_astar.py
# ============================================================
# TASK
#   Implement A* search that returns (path, cost).
#
# SIGNATURE (do not change):
#   astar(start, goal, neighbors_fn, heuristic_fn, trace) -> (List[Coord], float)
#
# PARAMETERS
#   start, goal:           grid coordinates
#   neighbors_fn(u):       returns valid 4-neighbors of u
#   heuristic_fn(u, goal): returns a non-negative estimate to goal
#   trace:                 MUST call trace.expand(u) whenever you pop u
#                         from the PRIORITY QUEUE to expand it.
#
# EDGE COSTS
#   Assume unit step cost (=1) unless your runner specifies otherwise.
#   (If your runner supplies a graph.cost(u,v), adapt here if needed.)
#
# RETURN
#   (path, cost) where path is the list of coordinates from start to goal,
#   and cost is the sum of step costs along that path (float).
#   If no path exists, return ([], 0.0).
#
# IMPLEMENTATION HINT
# - Use min-heap over f = g + h.
# - Keep g[u] (cost from start), parent map, and a closed set.
# - On goal, reconstruct path and also compute cost (sum of steps).
# ============================================================

from typing import List, Tuple, Callable, Dict
import heapq
import math

Coord = Tuple[int, int]

def astar(start: Coord,
          goal: Coord,
          neighbors_fn: Callable[[Coord], List[Coord]],
          heuristic_fn: Callable[[Coord, Coord], float],
          trace) -> Tuple[List[Coord], float]:
    """
    REQUIRED: call trace.expand(u) when you pop u from the PQ to expand.
    """
    # Handle trivial case
    if start == goal:
        trace.expand(start)
        return ([start], 0.0)
    
    # Initialize data structures
    g: Dict[Coord, float] = {start: 0.0}
    parent: Dict[Coord, Coord | None] = {start: None}
    closed: set = set()
    
    # Priority queue: (f_value, unique_counter, node)
    # Counter prevents comparison issues when f-values are equal
    counter = 0
    heap = []
    h_start = heuristic_fn(start, goal)
    heapq.heappush(heap, (h_start, counter, start))
    counter += 1
    
    while heap:
        f_val, _, u = heapq.heappop(heap)
        
        if u in closed:
            continue
        
        trace.expand(u)
        
        if u == goal:
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            
            cost = float(len(path) - 1)
            
            return (path, cost)
        
        closed.add(u)
        
        for v in neighbors_fn(u):
            if v in closed:
                continue
            
            tentative_g = g[u] + 1.0  
            
            if v not in g or tentative_g < g[v]:
                g[v] = tentative_g
                parent[v] = u
                
                h_v = heuristic_fn(v, goal)
                f_v = tentative_g + h_v
                
                heapq.heappush(heap, (f_v, counter, v))
                counter += 1
    
    return ([], 0.0)