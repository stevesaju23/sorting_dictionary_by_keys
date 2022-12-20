s={}
#where 3 is the number of values u want to enter in dictionary
for i in range(3):
    key=input("enter the key of dictionary")
    value=int(input("enter the value of the dictionary"))
    s[key]=value

s1={k: v for k,v in sorted(s.items())}
# sorting the dictionary by keys in asc^^^^^

s2={k: v for k,v in sorted(s.items(),reverse=True)}
# sorting the dictionary by keys in desc^^^^^

print(s1)
print(s2)
