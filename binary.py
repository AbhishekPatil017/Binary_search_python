# binary search using python

mylist=[10,6,7,8,1,2,3,4,5]


def binary_search(lst,item):
    #sorting list before performing binary search operation (binary search will only work in Ascending order for optimal operation)
    mylist.sort()

    # setting up index positions 
    low=0
    high=len(lst)-1
    print(mylist)

    # using while loop until the item is found in the sorted list
    while low <= high:
        
        # divding the list into 2 for fast search operation
        mid=(low+high)//2
        # creating temporary guess variable to find the item and returning the index position 
        guess=lst[mid]

        if guess == item:
            return mid
        if guess > item:
            high=mid-1
        else:
            low=mid+1

    return -1

print(binary_search(mylist,7))