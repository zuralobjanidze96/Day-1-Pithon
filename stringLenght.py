string = []
while len(string) < 5:
    print("Enter a string")
    string.append(input())

s = len(string[0])

for i in range(5):
    if s >= len(string[i]):
        continue
    else:
        s = len(string[i])
print("The length of the longest string is: ", s)




