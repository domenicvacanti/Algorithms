
def getHawkID():
    return ['dvacanti']

def pathExists(A, vertex1, vertex2):
    if vertex1 == vertex2:
        return True
    elif A[vertex1][vertex2] == 1:
            return True
    for i in range(len(A[vertex1])):
        if A[vertex1][i] == 1:
            A[vertex1][i] = 0
            if (pathExists(A, i, vertex2)):
                return True
    return False

def symmetricClosure(A):
    for i in range (len(A)):
        for j in range (len(A[i])):
            if A[i][j] == 1:
                A[j][i] =1
    return A

def antiSymmetric(A):
    for i in range (len(A)):
        for j in range (len(A[i])):
            if i == j:
                continue
            if A[i][j] == 1 and A[j][i] == 1:
                return False
    return True

def countBinaryStrings(n):
    list1 = []
    num1 = 2**n
    count = 0
    for i in range(num1):
        binNum = (format(i, "b"))
        if(len(binNum) < n+1):
            zeroCount = n-len(binNum)
            zeros = '0' * zeroCount 
        appendNum = zeros + binNum
        list1.append(appendNum)
    for num in list1:
        for i in range(len(num)):
            if i+1 >= len(num):
                continue
            if num[i] == '0' and num[i+1] == '0':
                count=count+1
                break
    return (len(list1)-count)

def prim(myList):
    for i in range(len(myList)):
        for j in range(len(myList[i])):
            if(myList[i][j]!= None):
                myList[i][j] = [myList[i][j],j,0,i]
    edges = []
    finalEdges = []
    for j in range(len(myList[0])):
        if myList[0][j]!=None:
            edges.append(myList[0][j])
    while (len(finalEdges) < len(myList)-1):
        min = [9999999999999,0,0,0]
        index = 0
        for i in range(len(edges)):
            if(edges[i][0] < min[0]):
                min[0] = edges[i][0]
                min[1] = edges[i][1]
                min[3] = edges[i][3]
                index = i
        del edges[index]
        min[2]=1
        myList[min[1]][min[3]][2] = 1
        myList[min[3]][min[1]][2] = 1
        finalEdges.append(min)
        for i in range (len(myList[finalEdges[-1][1]])):
            if(myList[finalEdges[-1][1]][i]!=None and myList[finalEdges[-1][1]][i][2]!=1):
                edges.append(myList[finalEdges[-1][1]][i])
    for i in range (len(myList)):
        for j in range (len(myList[i])):
            if(myList[i][j]!= None):
                if myList[i][j][2] == 0:
                    myList[i][j] = None
                else:
                    myList[i][j] = myList[i][j][0]
    return myList
