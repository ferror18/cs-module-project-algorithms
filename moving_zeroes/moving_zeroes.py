def verbose(myFunction, prt_able_i, do=True):
    if do:
        print(f'{myFunction.__name__} --> {prt_able_i}')
'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    i = len(arr)-1
    while i != -1:
        if arr[i] == 0:
            arr.append(arr.pop(i))
        if i == len(arr)-1:
            i-=1
        else:
            i-=1
    verbose(moving_zeroes, arr)
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")