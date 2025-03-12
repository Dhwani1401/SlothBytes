mapping = {
    "1" : "I",
    "2" : "Z",
    "3" : "E",
    "4" : "H",
    "5" : "S",
    "6" : "G",
    "7" : "L",
    "8" : "B",
    "0" : "O"
}

num = str(input("Enter the number:"))

ans = ""

for c in reversed(num):
    if(c in mapping):
        ans = ans + mapping[c]

print(ans)
