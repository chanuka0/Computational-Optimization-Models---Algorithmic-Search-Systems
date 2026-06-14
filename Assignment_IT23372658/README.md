# Computational Optimization Models & Algorithmic Search Systems

## 🎓 Student Information
* [cite_start]**Student ID:** IT23372658 [cite: 8]  
* **Module:** Intelligent Systems (SE3062)  
* [cite_start]**Assignment:** Individual Assignment 1 - Search & Optimization Models [cite: 3]

---

## 📊 Performance & Grading Summary
[cite_start]This implementation achieved a **100% Perfect Score** across all algorithmic modules[cite: 5]. [cite_start]The local test environment cross-checks optimization bounds, heuristic admissibility, and execution traces against strict hidden integrity checks[cite: 78, 86].

| Algorithmic Module | Status | Score | Metrics / Key Milestone Details |
| :--- | :---: | :---: | :--- |
| [cite_start]**Breadth-First Search (BFS)** [cite: 6] | [cite_start]✅ OK [cite: 5] | [cite_start]**10 / 10** [cite: 5] | [cite_start]Unweighted Path Length: 11/11 [cite: 5] |
| [cite_start]**A* Search** [cite: 13] | [cite_start]✅ OK [cite: 5] | [cite_start]**15 / 15** [cite: 5] | [cite_start]Expanded Nodes: 25 [cite: 5] |
| [cite_start]**Iterative Deepening Search (IDS)** [cite: 24] | [cite_start]✅ OK [cite: 5] | [cite_start]**15 / 15** [cite: 5] | [cite_start]Expanded Nodes: 163 [cite: 5] |
| [cite_start]**Simulated Annealing (SA)** [cite: 31] | [cite_start]✅ OK [cite: 5] | [cite_start]**15 / 15** [cite: 5] | [cite_start]Cost Reduction / Improvement: 6.00 [cite: 5] |
| [cite_start]**Heuristics Verification** [cite: 52] | [cite_start]✅ OK [cite: 5] | [cite_start]**20 / 20** [cite: 5] | [cite_start]Validated: Manhattan, Straight-Line, Custom [cite: 53] |
| [cite_start]**Linear Programming (LP)** [cite: 63] | [cite_start]✅ OK [cite: 5] | [cite_start]**12.5 / 12.5** [cite: 5] | [cite_start]Graphical Vertex Optima ($Z^* = 28$) [cite: 5, 69] |
| [cite_start]**Dynamic Programming (DP)** [cite: 70] | [cite_start]✅ OK [cite: 5] | [cite_start]**12.5 / 12.5** [cite: 5] | [cite_start]Knapsack Value Cross-Check ($Value = 29$) [cite: 5, 72] |
| **Total Score** | | **100 / 100** | |

---

## 🛠️ Algorithmic Design & Implementation Notes

### 1. Uninformed & Informed Search Algorithms
* **Breadth-First Search (`student_bfs.py`)**
  * Utilizes a standard First-In-First-Out (FIFO) queue architecture[cite: 11].
  * [cite_start]Guarantees the shortest path on an unweighted grid ($6 \times 6$ layout with 8 static obstacles)[cite: 8, 11].
  * [cite_start]Explicitly updates `trace.expand()` on each node extraction to maintain rigorous trace compliance[cite: 12].
* **A* Search (`student_astar.py`)**
  * Combines BFS completeness with greedy heuristic efficiency via the evaluation function $f = g + h$[cite: 21].
  * [cite_start]Leveraging an admissible Manhattan distance metric, it limits node expansions to 25 (a $7\%$ structural efficiency improvement over baseline search bounds)[cite: 14, 22, 23].
* **Iterative Deepening Search (`student_ids.py`)**
  * Blends the space efficiency of Depth-First Search (DFS) with the step-optimality of BFS[cite: 25, 29].
  * [cite_start]Sequentially explores explicit depth thresholds ($d = 0, 1, 2 \dots$), successfully resolving optimal paths at depth 11 without incurring state-memoization storage costs[cite: 29, 30].

### 2. Meta-Heuristics & Distance Estimations
* **Simulated Annealing (`student_sa.py`)**
  * Employs a stochastic search framework that selectively accepts worse intermediate states via an explicit temperature cooling schedule to successfully escape local optima[cite: 51]. 
  * [cite_start]Achieved a concrete cost optimization reducing grid trajectory weight from a baseline of 11.6 down to 5.6 (Improvement: 6.00)[cite: 33].
* **Heuristics Assessment (`heuristics.py`)**
  * [cite_start]**Manhattan & Straight-line (Euclidean) Distances:** Validated mathematically as admissible (never overestimating true cost-to-go) across all sample spaces ($neg = 0$, $above = 0$)[cite: 54, 60].
  * **Custom Mix Heuristic:** Integrates multiple metric constraints to deliver accelerated topological gradient direction while keeping solution path optimal[cite: 62].

### 3. Advanced Mathematical Optimization
* **Linear Programming (`student_lp_dp.py`)**
  * Formulates a continuous optimization task maximizing $Z = 3x + 5y$ subject to $Ax \le b, \; x \ge 0, \; y \ge 0$[cite: 65].
  * [cite_start]Evaluates extreme boundary intersections via a graphical corner-point execution loop[cite: 64, 68]. [cite_start]Proves the fundamental theorem of LP by identifying the absolute optimum at a feasible region vertex: $(x, y) = (1.0, 5.0)$ with $Z = 28$[cite: 69].
* **Dynamic Programming - 0/1 Knapsack (`student_lp_dp.py`)**
  * [cite_start]Solves a discrete combinatoric optimization context over an item capacity threshold of 10 with 5 items[cite: 71, 72].
  * [cite_start]Implements parallel structural paradigms: Memoized Top-Down recursion and Tabulated Bottom-Up matrix processing[cite: 71]. 
  * Both architectures maintain absolute convergence, matching validation results exactly at a maximized matrix yield value of 29[cite: 72, 77].

---

## 📂 Project Architecture

```markdown
Computational-Optimization-Models---Algorithmic-Search-Systems/
│
└── Assignment_IT23372658/
    ├── common.py           # Core utility structures, grid mappings, and trace handlers
    ├── heuristics.py       # Mathematical estimation functions (Manhattan, Euclidean, Custom)
    ├── student_bfs.py      # Breadth-First Search implementation
    ├── student_astar.py    # A* Informed Search algorithm
    ├── student_ids.py      # Iterative Deepening Search algorithm
    ├── student_sa.py       # Simulated Annealing engine and cooling frameworks
    ├── student_lp_dp.py    # Linear Programming solvers & Knapsack Dynamic Programming matrices
    ├── runner.py           # Core benchmarking script for processing solutions and seeds
    ├── problem.json        # Grid layout definition and problem space configurations
    └── results.json        # Auto-generated verification traces and output parameterss