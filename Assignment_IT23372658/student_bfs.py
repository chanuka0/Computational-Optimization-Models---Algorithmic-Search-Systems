# student_bfs.py
# ============================================================
# TASK
#   Implement Breadth-First Search that returns a SHORTEST path
#   (by number of steps) from start to goal on an UNWEIGHTED grid.
#
# SIGNATURE (do not change):
#   bfs(start, goal, neighbors_fn, trace) -> List[Coord]
#
# PARAMETERS
#   start: (r, c)      tuple for start cell
#   goal:  (r, c)      tuple for goal cell
#   neighbors_fn(u):   function returning valid 4-neighbors of u
#   trace:             object with method trace.expand(node)
#                      YOU MUST call trace.expand(u) each time you
#                      pop/remove u from the FRONTIER to expand it.
#
# RETURN
#   A list of coordinates [(r0,c0), (r1,c1), ..., goal].
#   If no path is found, return [].
#
# NOTES
# - Use a QUEUE (FIFO).
# - Keep a parent map: parent[child] = node we came from.
# - Reconstruct path when you first reach goal.
# - You may print debug info; the runner will still grade correctly.
# ============================================================

from typing import List, Tuple, Callable, Dict
from collections import deque

Coord = Tuple[int, int]

def bfs(start: Coord,
        goal: Coord,
        neighbors_fn: Callable[[Coord], List[Coord]],
        trace) -> List[Coord]:
    """
    Implement classic BFS on an unweighted grid/graph.
    REQUIRED: call trace.expand(u) when you pop u from the queue.
    """
    if start == goal:
        trace.expand(start)
        return [start]
    
    queue = deque([start])
    parent: Dict[Coord, Coord | None] = {start: None}
    
    while queue:
        u = queue.popleft()
        
        trace.expand(u)
        
        if u == goal:
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        
        for v in neighbors_fn(u):
            if v not in parent:
                parent[v] = u
                queue.append(v)
    
    return []