import heapq

def a_star_search(start, goal, maze):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(node):
        neighbors = []
        x, y = node
        if x > 0 and maze[y][x - 1] == 0:
            neighbors.append((x - 1, y))
        if x < len(maze[0]) - 1 and maze[y][x + 1] == 0:
            neighbors.append((x + 1, y))
        if y > 0 and maze[y - 1][x] == 0:
            neighbors.append((x, y - 1))
        if y < len(maze) - 1 and maze[y + 1][x] == 0:
            neighbors.append((x, y + 1))
        return neighbors

    def reconstruct_path(came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_list]:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return []
