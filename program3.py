def longest_prefix_suffix_length(s):
    n=len(s)
    lps = [0]*n
    j=0
    for i in range (1,n):
        while j >0 and s[i] !=s[j]:
            j=lps[j-1]
        if s[i] == s[j]:
            j +=1
        lps[i] =1
    length = lps[-i]
    return length
input_string = input("Enter a string: ")
result = longest_prefix_suffix_length(input_string)
print("Lengthoflongestproper prefix same as suffix:",result)
        
         
          
                 