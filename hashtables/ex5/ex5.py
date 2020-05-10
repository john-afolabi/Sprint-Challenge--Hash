def finder(files, queries):
    """
    YOUR CODE HERE
    """
    hastable = {}
    result = []

    for i, string in enumerate(files):
        words = string.split("/")[1:]
        for word in words:
            if word in hastable:
                hastable[word].append(i)
            else:
                hastable[word] = [i]
    for word in queries:
        if word in hastable:
            indexes = hastable[word]
            for index in indexes:
                result.append(files[index])
    return result


if __name__ == "__main__":
    files = ['/bin/foo', '/bin/bar', '/usr/bin/baz', '/tre/bin/foo']
    queries = ["foo", "qux", "baz"]
    print(finder(files, queries))
