def recursive_digit_sum(n,k):
    def digit_sum(num):
        if num<10:
            return num
        else:
            return num % 10+ digit_sum(num //10)
    intial_sum=digit_sum(n)*k
    if intial_sum>9 and k>1:
        return recursive_digit_sum(intial_sum,1)
    else:
        return intial_sum
n=9875
k=4
result=recursive_digit_sum(n,k)
print(result)
        

