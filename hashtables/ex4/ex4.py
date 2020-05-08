def has_negatives(a):
    """
    YOUR CODE HERE
    """

    hashtable = {}
    result = []
    for i, num in enumerate(a):
        hashtable[abs(num)] = i
        # print(hashtable)
        if num not in hashtable:
            result.append(abs(num))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
