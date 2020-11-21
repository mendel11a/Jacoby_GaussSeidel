# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

def jacoby(a, x, b):
    # Finding length of a(3)
    n = len(a)
    # for loop for 3 times as to calculate x, y , z
    y=[0 for a in x]
    for j in range(0, n):
        # temp variable d to store b[j]
        d = b[j]

        # to calculate respective xi, yi, zi
        for i in range(0, n):
            if (j != i):
                d -= a[j][i] * x[i]
                # updating the value of our solution
        y[j] = d / a[j][j]
        # returning our updated solution

    return y


def calsEps(x,y,eps):
    for i in range(len(x)):
        if abs(x[i]-y[i])>eps:
            return True
    return False


def mainSeidel(a,x,b,eps):
    first=[eps+1 for a in x]
    iter=0
    while(calsEps(x,first,eps)):
        iter=iter+1
        first = [a for a in x]
        x = jacoby(a, x, b)
        #print each time the updated solution
        print(x)
    print(x)
    print("number of itertion="+ str(iter))

def isDDM(a, n):
    # for each row
    for i in range(0, n):

        # for each column, finding
        # sum of each row.
        sum = 0
        for j in range(0, n):
            sum = sum + abs(a[i][j])

            # removing the
        # diagonal element.
        sum = sum - abs(a[i][i])

        # checking if diagonal
        # element is less than
        # sum of non-diagonal
        # element.
        if (abs(a[i][i]) < sum):
            print("Non-dominant diagonal")

    print("Dominant diagonal")



# int(input())input as number of variable to be solved
n = 3
a = []
b = []
# initial solution depending on n(here n=3)
x = [0, 0, 0]
a = [[4, 1, 2], [3, 5, 1], [1, 1, 3]]
b = [4, 7, 3]
print(x)
eps=0.001
# loop run for m times depending on m the error value


isDDM(a, n)
mainSeidel(a,x,b,eps)
