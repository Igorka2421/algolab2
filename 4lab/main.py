from collections import deque

def find_shortest_path(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    visited = set()

    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 1 and (nx, ny) not in visited:
                queue.append((nx, ny, steps + 1))
                visited.add((nx, ny))

    return -1

def main():

    with open('input.txt', 'r') as file:
        start_line = file.readline().strip()
        end_line = file.readline().strip()
        size_line = file.readline().strip()


        if not start_line or not end_line or not size_line:
            print("Error: One or more lines in the input file are empty.")
            return

        start = tuple(map(int, start_line.split(', ')))
        end = tuple(map(int, end_line.split(', ')))
        rows, cols = map(int, size_line.split(', '))
        matrix = [list(map(int, file.readline().strip()[1:-1].split())) for _ in range(rows)]


    shortest_path = find_shortest_path(matrix, start, end)


    with open('output.txt', 'w') as file:
        file.write(str(shortest_path))

if __name__ == "__main__":
    main()


