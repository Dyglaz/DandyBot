def script(check, x, y):
    if check("gold", x, y):
        return "take"
    return movement(check, x, y)

def movement(check, x, y):
    path = goldSearch(check, x, y)
    (x_, y_), (dx, dy) = path[:2]
    match (dx - x_, dy - y_):
        case (-1, 0):
            return "left"
        case (1, 0):
            return "right"
        case (0, -1):
            return "up"
        case (0, 1):
            return "down"

def goldSearch(check, x, y):
    visitedPath  = {(x, y)}
    queuePath = [[(x, y)]]
    while queuePath:
        path = queuePath.pop(0)
        x_, y_ = path[-1]
        if check("gold", x_, y_):
            return path
        for dx, dy in [(x_ - 1, y_), (x_ + 1, y_), (x_, y_ - 1), (x_, y_ + 1)]:
            if not check("wall", dx, dy) and (dx, dy) not in visitedPath:
                visitedPath .add((dx, dy))
                queuePath.append(path + [(dx, dy)])