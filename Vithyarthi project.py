from collections import deque
maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '#', '.', 'E']
]

def print_maze(maze, path=None):
    maze_copy = [row[:] for row in maze]
    
    if path:
        for r, c in path:
            if maze_copy[r][c] not in ('S', 'E'):
                maze_copy[r][c] = '*'
                
    for row in maze_copy:
        print(" ".join(row))
    print("\n")

def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    start_pos = None
    
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start_pos = (r, c)
                break
                
    if not start_pos:
        return "No Start point found!"

    queue = deque([(start_pos, [start_pos])])
    
    visited = set()
    visited.add(start_pos)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    while queue:
        current_pos, path = queue.popleft()
        curr_r, curr_c = current_pos
        
        if maze[curr_r][curr_c] == 'E':
            return path 
            
        for dr, dc in directions:
            next_r, next_c = curr_r + dr, curr_c + dc
            
            if 0 <= next_r < rows and 0 <= next_c < cols:
                if maze[next_r][next_c] != '#' and (next_r, next_c) not in visited:
                    
                    visited.add((next_r, next_c))
                    
                    new_path = path + [(next_r, next_c)]
                    queue.append(((next_r, next_c), new_path))
                    
    return None 

print("--- UNsolved Maze ---")
print_maze(maze)

print("AI is searching for the shortest path...\n")
winning_path = solve_maze(maze)

if winning_path:
    print("--- SOLVED Maze ---")
    print("The AI found the exit! Path is marked with '*'")
    print_maze(maze, winning_path)
    print(f"Total steps taken: {len(winning_path) - 1}")
else:
    print("This maze has no valid exit path!")