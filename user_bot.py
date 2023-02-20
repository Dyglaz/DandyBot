def script(check, x, y):
    if check("gold", x, y):
        return "take"
    return solve(check, x, y)


def solve(check, x, y):
    path = find_gold_iter(check, x, y)
    (x_, y_), (dx, dy) = path[:2]
    direction = {(-1, 0): "left", (1, 0): "right", (0, -1): "up", (0, 1): "down"}
    return direction[(dx - x_, dy - y_)]


def find_gold_iter(check, x, y):
    visited = {(x, y)}
    queue = [[(x, y)]]
    while queue:
        path = queue.pop(0)
        x_, y_ = path[-1]
        if check("gold", x_, y_):
            return path
        for dx, dy in [(x_ - 1, y_), (x_ + 1, y_), (x_, y_ - 1), (x_, y_ + 1)]:
            if not check('wall', dx, dy) and (dx, dy) not in visited:
                visited.add((dx, dy))
                queue.append(path + [(dx, dy)])