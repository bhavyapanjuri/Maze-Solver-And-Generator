# 🧩 Maze Solver & Generator

A simple Python program that generates random mazes and finds the shortest path using BFS algorithm.

## ✨ Features

- Random maze generation using Recursive Backtracking
- Shortest path solver using BFS (Breadth-First Search)
- Console visualization with ASCII characters
- Single file - no external dependencies
- Input validation (minimum 5×5 maze)

## 🚀 Usage

Run the program:
```bash
python maze_solver.py
```

Enter maze dimensions when prompted:
```
Enter maze height (min 5): 11
Enter maze width (min 5): 21
```

## 📋 Requirements

- Python 3.7 or higher
- No external libraries needed (uses only built-in modules: `random`, `collections`)

## 🎨 Output Example

```
# # # # # # # # # # # # # # #
# S * * * # . . . # . . . . #
# # # . # # # . # # . # # . #
# . . . . . # . . . . # . . #
# . # # # # # # # # # # # . #
# . . . . . . . * * * * * . #
# # # # # . # # # # # # * # #
# . . . . . # . . . . . * E #
# # # # # # # # # # # # # # #

Path length: 24 steps

 Solution found!
```

**Legend:**
- `S` = Start point
- `E` = End point
- `*` = Solution path
- `#` = Wall
- `.` = Open path

## 🔧 How It Works

1. **Maze Generation**: Uses Recursive Backtracking algorithm to create a perfect maze (one unique path between any two points)
2. **Path Finding**: BFS algorithm guarantees the shortest path from start to end
3. **Visualization**: Displays the maze and solution in the console

## 📂 Project Structure

```
Maze_Solver&Generator/
├── maze_solver.py    # Complete program (95 lines)
└── README.md         # Documentation
```

## 💡 Use Cases

- Learning pathfinding algorithms
- Game development practice
- Algorithm visualization
- Coding interview preparation

## 📝 License

Open source - free to use and modify

---

## 💻 Code Explanation

### Class Structure

```python
class MazeSolver:
    def __init__(self, rows, cols):
```

**Initialization:**
- Converts even dimensions to odd (maze generation requires odd dimensions)
- Creates a 2D grid filled with walls (1 = wall, 0 = path)
- Sets start point at (1, 1) and end point at (rows-2, cols-2)

### Maze Generation Algorithm

```python
def generate(self):
    """Generate maze using recursive backtracking"""
```

**Recursive Backtracking (DFS-based):**
1. Start with a grid full of walls
2. Begin at start position and mark as path
3. Use a stack to track current path
4. For each cell:
   - Find unvisited neighbors (2 cells away)
   - Randomly pick one neighbor
   - Remove wall between current and neighbor
   - Move to neighbor and repeat
5. Backtrack when no unvisited neighbors exist

**Why 2 cells away?** Creates walls between paths, ensuring proper maze structure.

### Path Finding Algorithm

```python
def solve_bfs(self):
    """Solve maze using BFS"""
```

**Breadth-First Search (BFS):**
1. Use a queue (FIFO) to explore cells level by level
2. Start from start position
3. For each cell:
   - Check all 4 neighbors (up, down, left, right)
   - Add unvisited valid neighbors to queue
   - Track the path taken to reach each cell
4. Stop when end position is reached
5. Return the path

**Why BFS?** Guarantees the shortest path because it explores all cells at distance N before exploring cells at distance N+1.

### Visualization

```python
def display(self, path=None):
    """Display maze"""
```

**Display Logic:**
- Iterate through each cell in the grid
- Print different characters based on cell type:
  - `S` for start position
  - `E` for end position
  - `*` for solution path cells
  - `#` for walls
  - `.` for open paths

### Data Structures Used

1. **2D List (Grid):** Represents the maze structure
   ```python
   self.grid = [[1] * cols for _ in range(rows)]
   # 1 = wall, 0 = path
   ```

2. **Stack (List):** For maze generation (DFS)
   ```python
   stack = [self.start]  # LIFO - Last In First Out
   ```

3. **Queue (deque):** For pathfinding (BFS)
   ```python
   queue = deque([(self.start, [self.start])])  # FIFO - First In First Out
   ```

4. **Set:** Track visited cells (O(1) lookup)
   ```python
   visited = {self.start}  # Fast membership testing
   ```

5. **Tuple:** Store coordinates
   ```python
   (row, col)  # Immutable position representation
   ```

### Algorithm Complexity

**Maze Generation:**
- Time: O(rows × cols) - visits each cell once
- Space: O(rows × cols) - stores the grid

**BFS Pathfinding:**
- Time: O(rows × cols) - worst case visits all cells
- Space: O(rows × cols) - queue and visited set

### Key Concepts

1. **Perfect Maze:** Every cell is reachable from every other cell via exactly one path
2. **Recursive Backtracking:** DFS-based algorithm that carves paths by removing walls
3. **BFS Guarantee:** Always finds shortest path in unweighted graphs
4. **Grid Representation:** 0 = passable, 1 = wall

### Input Validation

```python
if rows < 5 or cols < 5:
    print(" Enter Minimum 5x5\n")
```

**Why minimum 5×5?**
- Ensures enough space for meaningful maze generation
- Prevents trivial mazes where start = end
- Allows proper wall and path structure
- Smaller sizes (2×2, 3×3, 4×4) result in start and end being the same position

### Variable Naming Convention

**Common variables used in grid traversal:**

```python
r, c    →  row, column (current position)
dr, dc  →  delta row, delta column (change in position)
nr, nc  →  new row, new column (next position)
```

**Direction Movements:**

```python
[(0, 1), (1, 0), (0, -1), (-1, 0)]
  ↓      ↓       ↓        ↓
 RIGHT  DOWN    LEFT     UP
```

**Breakdown:**
- `(0, 1)` → dr=0, dc=1 → Move RIGHT (same row, +1 column)
- `(1, 0)` → dr=1, dc=0 → Move DOWN (+1 row, same column)
- `(0, -1)` → dr=0, dc=-1 → Move LEFT (same row, -1 column)
- `(-1, 0)` → dr=-1, dc=0 → Move UP (-1 row, same column)

**Example Calculation:**

```python
# Current position
r, c = 5, 5

# Moving RIGHT: dr=0, dc=1
nr = r + dr = 5 + 0 = 5  # new row stays same
nc = c + dc = 5 + 1 = 6  # new column increases

# Result: moved from (5,5) to (5,6) → RIGHT
```

**Visual Grid Example:**

```
     col 0  col 1  col 2
row 0  [ ]    [ ]    [ ]
row 1  [ ]    [X]    [ ]  ← Current position (r=1, c=1)
row 2  [ ]    [ ]    [ ]

Moving RIGHT (dr=0, dc=1):
row 1  [ ]    [X]    [→]  ← New position (nr=1, nc=2)
```

**In Code Context:**

```python
for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Try all 4 directions
    nr, nc = r + dr, c + dc  # Calculate new position
    if is_valid(nr, nc):     # Check if new position is valid
        visit(nr, nc)        # Move to new position
```

## 🎯 Code Statistics

- **Total Lines:** 95
- **Class Methods:** 3 (generate, solve_bfs, display)
- **Dependencies:** 2 built-in modules (random, collections)
- **Time Complexity:** O(rows × cols)
- **Space Complexity:** O(rows × cols)
