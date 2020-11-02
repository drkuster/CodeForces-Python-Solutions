def inlt():
    return(list(map(int,input().split())))

def find_dominant(Tank):
    largest = max(Tank)
    for i in range(0, len(Tank)):
        if Tank[i] == largest:
            if i == 0:
                if Tank[i + 1] < Tank[i]:
                    return i + 1
            elif i == len(Tank) - 1:
                if Tank[i - 1] < Tank[i]:
                    return i + 1
            else:
                if Tank[i - 1] < Tank[i] or Tank[i + 1] < Tank[i]:
                    return i + 1
    return -1
                
t = int(input())
for i in range(0, t):
    int(input())
    Tank = inlt()
    print(find_dominant(Tank))