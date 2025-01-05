# An array b1,b2,…,bn
#  of positive integers is good if all the sums of two adjacent elements are equal to the same value. More formally, the array is good if there exists a k
#  such that b1+b2=b2+b3=…=bn−1+bn=k
# .

# Doremy has an array a
#  of length n
# . Now Doremy can permute its elements (change their order) however she wants. Determine if she can make the array good.

# Input
# The input consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤100
# ) — the number of test cases. The description of the test cases follows.

# The first line of each test case contains a single integer n
#  (2≤n≤100
# ) — the length of the array a
# .

# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤105
# ).

# There are no constraints on the sum of n
#  over all test cases.

# Output
# For each test case, print "Yes" (without quotes), if it is possible to make the array good, and "No" (without quotes) otherwise.

# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
def check(arr):
    if len(set(arr))>2:
        return "No"
    counter1 = 1
    n = len(arr)
    for i in range(1, len(arr)):
        if arr[i] == arr[0]:
            counter1 += 1
    if counter1 == n:
        return "Yes"
    counter2 = n - counter1
    if abs(counter1-counter2)>1:
        return "No"
    return "Yes"


if __name__ == '__main__':
    t = int(input())
    inputs = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split(" ")))
        inputs.append(arr)
    

    for i in inputs:
        print(check(i))

