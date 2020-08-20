def verbose(myFunction, prt_able_i, do=False):
    if do:
        print(f'{myFunction.__name__} --> {prt_able_i}')
'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    tarr = []
    for i in range(len(arr)):
        y = 1
    #transformation
        for x in range(len(arr)):
            if i != x:
                y = y * arr[x]
            verbose(product_of_all_other_numbers,{'i':arr[i], 'x':arr[x], 'y':y})
    #prepare setup
        tarr.append(y)
        verbose(product_of_all_other_numbers, ('\t ^^^ Included ^^^'))
    # tarr = tarr[::-1]
    verbose(product_of_all_other_numbers, ('\t\n\n ^^^ END ^^^\n\n'))
    return tarr

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5] # result --> [120, 60, 40, 30, 24]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
