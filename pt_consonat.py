s="Engineering"
res=""
for val in s:
    if 'a'<=val<='z' or 'A'<=val<='Z':
        if val in "AEIOUaeiou" or  val in res:
            res+=val
print(res)
