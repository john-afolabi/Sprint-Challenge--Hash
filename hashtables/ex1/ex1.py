def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    hashtable = {}

    for i, weight in enumerate(weights):
        if weight in hashtable:
            value = hashtable[weight]
            return [i, value]
        diff = limit - weight
        hashtable[diff] = i
    return None