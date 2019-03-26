Q_value = -0.04
R_Value = 10
Out_Bounds = -0.04
Grid = []


def gen_grid(m, n):  # generate grid world
    for i in range(m):
        row = []
        for j in range(n):
            row.append(0)
        Grid.append(row)
    Grid[0][n-1] = R_Value
    Grid[1][n-1] = -1*R_Value


def make_grid(g):
    for r in g:
        print(r)


def Q_tile(q):
    for i in range(q):
        x, y = input("Enter a b for q{} ".format(str(i))).split(' ')
        Grid[int(x)][int(y)] = Q_value


def policy(x, y, m, n):

    up, left, right, down = None, None, None, None


    if x - 1 < 0: # up
        up = Out_Bounds
    else:
        up = Grid[x - 1][y]


    if x + 1 > m - 1: # down
        down = Out_Bounds
    else:
        down = Grid[x + 1][y]


    if y - 1 < 0: # left
        left = Out_Bounds
    else:
        left = Grid[x][y - 1]

    if y + 1 > n - 1: # right
        right = Out_Bounds
    else:
        right = Grid[x][y + 1]

    return up, down, left, right

def calc_policy(up, down, left, right):

    return max(
        0.8*up + 0.1*left + 0.1*right,
        0.8*right + 0.1*up + 0.1*down,
        0.8*down + 0.1*right + 0.1*left,
        0.8*left + 0.1*down + 0.1*up
    )

def optim_calculation(m, n, k): # optimal policy
    for _ in range(k):
        for i, z in enumerate(Grid):
            for j, _ in enumerate(z):
                if Grid[i][j] != Out_Bounds and Grid[i][j] != Q_value:
                    u, d, l, r = policy(i, j, m, n)
                    v_star = calc_policy(u, d, l, r)
                    Grid[i][j] = v_star
                    Grid[0][n - 1] = R_Value
                    Grid[1][n - 1] = -1 * R_Value


M = 3 # change these for row
N = 4  # change change these column

gen_grid(M, N)
make_grid(Grid)
Q_tile(1) # change value to enter q amount
make_grid(Grid)
optim_calculation(M, N, 100)
make_grid(Grid)
