num = 121
temp = num 
reverse = 0 

# Loop runs completely to reverse the entire number

while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp //10
    
# Check happens ONLY ONCE after the loop finishes

if num == reverse:
        print ("Palindrome")

else :
            print ("Non Palindrome")