import random
from collections import deque

class MazeSolver:
    def __init__(self, rows, cols):
        # Make dimensions odd
        self.rows = rows if rows % 2 == 1 else rows + 1
        self.cols = cols if cols % 2 == 1 else cols + 1
        self.grid = [[1] * self.cols for _ in range(self.rows)]
        self.start = (1, 1)
        self.end = (self.rows - 2, self.cols - 2)
        
    def generate(self):
        """Generate maze using recursive backtracking"""
        stack = [self.start]
        self.grid[self.start[0]][self.start[1]] = 0
        
        while stack:
            current = stack[-1]
            neighbors = []
            
            # Check 4 directions (2 cells away)
            for dr, dc in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
                nr, nc = current[0] + dr, current[1] + dc
                if 0 < nr < self.rows - 1 and 0 < nc < self.cols - 1 and self.grid[nr][nc] == 1:
                    neighbors.append((nr, nc))
            
            if neighbors:
                next_cell = random.choice(neighbors)
                # Remove wall between current and next
                self.grid[(current[0] + next_cell[0]) // 2][(current[1] + next_cell[1]) // 2] = 0
                self.grid[next_cell[0]][next_cell[1]] = 0
                stack.append(next_cell)
            else:
                stack.pop()
        
        self.grid[self.end[0]][self.end[1]] = 0
    
    def solve_bfs(self):
        """Solve maze using BFS"""
        queue = deque([(self.start, [self.start])])
        visited = {self.start}
        
        while queue:
            (r, c), path = queue.popleft()
            if (r, c) == self.end:
                return path
            
            # Check 4 directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols and \
                   self.grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
        return None
    
    def display(self, path=None):
        """Display maze"""
        path_set = set(path) if path else set()
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) == self.start:
                    print('S', end=' ')
                elif (i, j) == self.end:
                    print('E', end=' ')
                elif (i, j) in path_set:
                    print('*', end=' ')
                elif self.grid[i][j] == 1:
                    print('#', end=' ')
                else:
                    print('.', end=' ')
            print()
        if path:
            print(f"\nPath length: {len(path)} steps")

if __name__ == "__main__":
    print("🧩 MAZE SOLVER & GENERATOR\n")
    
    while True:
        try:
            rows = int(input("Enter maze height (min 5): "))
            cols = int(input("Enter maze width (min 5): "))
            if rows < 5 or cols < 5:
                print(" Enter Minimum 5x5\n")
                continue
            break
        except ValueError:
            print(" Invalid input\n")
    
    print("\n Generating maze...")
    maze = MazeSolver(rows, cols)
    maze.generate()
    
    print(" Solving maze...\n")
    path = maze.solve_bfs()
    
    if path:
        maze.display(path)
        print("\n Solution found!")
    else:
        print(" No solution found!")
