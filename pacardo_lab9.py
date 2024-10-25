rows = int(input("Enter the number of rows: "))
num = 1  
for r in range(1, rows + 1):
    for c in range(1, r + 1):
        print(num, end=" ")
        num += 1  
    print() 
