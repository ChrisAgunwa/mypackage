def top_n (items, n):
    """Returns the top n of array in descending order

    Args:
        items (array): list or arrays_like object
        n (int): num of items to return
    
    Return:
        array: top n items in desc order
    
    Egs:
        >>> top_n([8, 3, 5, 1, 2], 3)
        [8, 5, 3]
    """
    for i in range(n):
        for j in range(len(items)-1-i):
            if item[j] > item[j+1]:
                item[j], item[j+1] = item[j+1], item[j]

    top_n = items[-n:]
    
    return top_n[::-1]
    
                