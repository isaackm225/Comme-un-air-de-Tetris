def read_grid(path):
   with open(path, "r") as f1:
        contenu = f1.readlines()
        grid = []
        for ligne in contenu:
            L = []
            for i in ligne:
                if i != "\n" and i != " ":
                    L.append(int(i))
            grid.append(L)
        f1.close()
   return grid

def save_grid(path,grid):

     with open(path, "w") as f:
        for row in grid:
            for elem in row:
                f.write(str(elem) + " ")
            f.write("\n")
        f.close()

def print_grid(grid):
    for row in grid:
        for elem in row:
            if elem == 0:
                print(chr(32), end=" ")
            elif elem == 1:
                print(chr(46), end=" ")
            else:
                print(chr(35), end=" ")
        print()

def print_blocs(blocs_l):
    for liste in range(55):
        for j in range(5):
            for i in range(5):
                if blocs_l[liste][j][i] == 0:
                   print(chr(32), end=" ")
                elif blocs_l[liste][j][i] == 1:
                    print('■', end=" ")
            print()

        print()
        print()

grid = read_grid("losange.txt")
print_blocs(grid)