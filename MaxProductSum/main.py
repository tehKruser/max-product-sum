def MaxProdSum(Array):
    MaxArray = []

    for i in range(0, len(Array)):
        if (i==0):
            MaxArray.append(Array[i])
        elif(i==1):
            val1 = Array[i]*Array[i-1]
            val2 = Array[i]+Array[i-1]
            max_val = max(val1, val2)
            MaxArray.append(max_val)
        else:
            val1 = Array[i] * Array[i - 1] + MaxArray[i-2]
            val2 = Array[i] + MaxArray[i-1]
            max_val = max(val1, val2)
            MaxArray.append(max_val)
    return MaxArray[-1]

myArr = [1, 4, 3, 2, 3, 4, 2]

print("Max product sum:", MaxProdSum(myArr))