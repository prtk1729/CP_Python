


if __name__ == "__main__":
    li = [2, 3, 5, 16, 17, 1]

    # Some opns
    li2 = sorted(li) # outplace sort O(nlogn)
    print(li2) # [1, 2, 3, 5, 16, 17]
    print()
    li.sort() # inplace sort O(nlogn)
    print(li2) # [1, 2, 3, 5, 16, 17]
    print(li) # [1, 2, 3, 5, 16, 17]

    # slicing opns

    i, j = 2, 5
    print( len(li) ) # 6, O(1)
    print( li[i] ) # 3, O(1)

    # slicing with j excluding, O(n), n is size(li)
    li3 = li[i : j] 
    print(li3) # [3, 5, 16]
    print()

    # Every kth element in a subarray
    k = 2
    li4 = li[i:j:k] 
    print(li4) # [3, 16]
    print()

    # reversing a list
    li5 = li[::-1]
    print(li5) # [17, 16, 5, 3, 2, 1]
    print()

    # print ;ast 4 elements
    li6 = li[-4:] # in usual order
    print(li6) # [3, 5, 16, 17]
    print()

    # pop the last element
    li.pop()
    print(li) # [1, 2, 3, 5, 16], NOTE: 17 popped
    print()

    # add 1 elem to the end
    li.append(14)
    print(li) # [1, 2, 3, 5, 16, 14], NOTE: 14 appended
    print()


    # prefix uptil index i (excluding "i")
    li6 = li[:i]
    print(li6) # [1, 2]
    print()


    # suffix from index k( here 2) till end
    li7 = li[k:]
    print(li7) # [3, 5, 16, 14]
    print()



