#Counting words occurenece in string
str1 = "big black bug bit a big black dog on his big black nose"
ls =str1.split(' ')
set_ls = set(ls)
for item in set_ls:
    print(item)
    count = ls.count(item)
    print(count)
