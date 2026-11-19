import os, random, time

W, H = 65, 28
CENTER = W // 2
TOP, BOTTOM = 2, 28

# 树叶形状
leaf = set()
for y in range(TOP, BOTTOM + 1):
    half = y - TOP
    for x in range(CENTER - half, CENTER + half + 1):
        leaf.add((x, y))

# 树干
trunk = set()
for y in range(BOTTOM + 1, BOTTOM + 4):
    for x in range(CENTER - 1, CENTER + 2):
        trunk.add((x, y))

# 颜色配置
GREEN, GOLD, WHITE, RESET = "\033[92m", "\033[93m", "\033[97m", "\033[0m"
LIGHTS = ["\033[91m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]

def frame(skip):
    snow = [(random.randint(0, W-1), random.randint(0, H-1)) for _ in range(200)]
    lights = {(x, y): random.choice(LIGHTS) for (x, y) in random.sample(list(leaf), 20)}
    for y in range(H):
        line = ""
        for x in range(W):
            if (x, y) in leaf:
                line += lights.get((x, y), GREEN) + "*" + RESET
            elif (x, y) in trunk:
                line += GOLD + "|" + RESET
            elif (x, y) in snow:
                line += WHITE + "·" + RESET
            else:
                line += " "
        print(line)
    time.sleep(0.1)
    os.system("cls" if os.name == "nt" else "clear")

while True:
    frame(False)
