import random
import queue
import time
OBSTCL = "#"
PSBL = " "
START = "O"
FINISH = "X"
ROWS = 50
COLS = 50


def print_map(map, path):
    trues = 0
    print(f"path: {path}")
    for i in range(len(map)):
        for j in range(len(map[0])):
            
            if (i, j) in path:
                trues += 1
                print("x ", end = "")
            else:
                print(f"{map[i][j]} ", end = "")
        print()
    print(f"trues: {trues}")

def get_start(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == START:
                return i, j
            
    return None


def find_path(map):
    start = get_start(map)
    # print(start)
    q = queue.Queue()
    q.put((start, [start]))
    visited = set()
    iter = 0
    while not q.empty():
        print(f"Iteration: {iter}")
        cur_pos, cur_path = q.get()
        #print(cur_pos, cur_path)
        x, y = cur_pos
        print_map(map, cur_path)
        time.sleep(0.1)
        if map[x][y] == FINISH:
            return cur_path
        neighbours = get_neighbours(map, cur_pos)
        for neighbour in neighbours:
            x1, y1 = neighbour
            if not (neighbour in visited or map[x1][y1] == OBSTCL):
                #print(f"current path: {cur_path}")
                new_path = cur_path + [neighbour]
                #cur_path.append(neighbour)
                #print(f"new path: {cur_path}")
                q.put((neighbour, new_path))
                visited.add(neighbour)
        iter += 1



def get_neighbours(map, cur):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            
            if abs(i + j) == 1:
                x, y = cur
                if in_range(x + i, y + j, map):
                    neighbours.append((x + i, y + j))

    return neighbours

def in_range(x, y, map):
    return 0 <= x <= len(map) and 0 <= y <= len(map[0])

def map_gen():
    choize = [" ", "#"]
    mapp = [["0" for _ in range(COLS)] for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            mapp[i][j] = random.choice(choize) 

    x1, y1 = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
    mapp[x1][y1] = "O"
    x2, y2 = x1, y1
    while (x2 == x1 and y2 == y1):
        x2, y2 = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
    mapp[x2][y2] = "X"
    print(f"start: {x1}, {y1}")
    print(f"finish: {x2}, {y2}")
    return mapp


def main():

    maze = [
        ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
    ]
    
    find_path(maze)
    

if __name__ == "__main__":
    main()