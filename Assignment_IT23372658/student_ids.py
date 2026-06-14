# student_ids.py - CORRECT VERSION
# ============================================================
# TASK
#   Implement Iterative Deepening Search (IDS).
#
# SIGNATURE (do not change):
#   ids(start, goal, neighbors_fn, trace, max_depth=64) -> (List[Coord], int)
#
# PARAMETERS
#   start, goal:       coordinates
#   neighbors_fn(u):   returns valid 4-neighbors of u
#   trace:             MUST call trace.expand(u) when you EXPAND u
#                      in the depth-limited search (DLS).
#   max_depth:         upper cap for the iterative deepening
#
# RETURN
#   (path, depth_limit_used)
#   - If found at depth L, return the path and L.
#   - If not found up to max_depth, return ([], max_depth).
#
# KEY FIX: 
#   - CRITICAL: Parent map must NOT persist stale pointers across branches!
#   - Use a LOCAL parent chain passed through recursion, not global dict
#   - This prevents cycles when backtracking
# ============================================================

from typing import List, Tuple, Callable, Set
from collections import deque

Coord = Tuple[int, int]

def ids(start: Coord,
        goal: Coord,
        neighbors_fn: Callable[[Coord], List[Coord]],
        trace,
        max_depth: int = 64) -> Tuple[List[Coord], int]:
    """
    Iterative Deepening Search using BFS within each depth level.
    
    This finds the optimal path because:
    1. At each depth limit, we explore level-by-level (BFS style)
    2. First path found at depth d is guaranteed to be at exactly depth d
    3. First depth where path is found has shortest path
    
    Returns (path, depth_limit_found).
    """
    
    for depth_limit in range(max_depth + 1):
        queue = deque([(start, [start], 0)])  # (node, path, current_depth)
        seen: Set[Coord] = {start}
        
        while queue:
            u, path, depth = queue.popleft()
            
            trace.expand(u)
            
            if u == goal:
                return (path, depth_limit)
            
            if depth < depth_limit:
                for neighbor in neighbors_fn(u):
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, path + [neighbor], depth + 1))
    
    return ([], max_depth)