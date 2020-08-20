def verbose(myFunction, prt_able_i, do=True):
    if do:
        print(f'{myFunction.__name__} --> {prt_able_i}')
# from itertools import product
'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, m=0):
    # Your code here
    temp = 0
    res = [1]  
    m = 3 
    for i in range(1, n + 1): 
        s = i - m - 1
        e = i - 1
        if (s >= 0): 
            temp -= res[s]  
        temp += res[e]  
        res.append(temp)  
          
    return res[n] 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
