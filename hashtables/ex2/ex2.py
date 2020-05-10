#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    hashtable = {}
    route = [None] * length

    for ticket in tickets:
        hashtable[ticket.source] = ticket.destination

    start = hashtable["NONE"]
    route[0] = start
    for i in range(1, len(route)):
        route[i] = hashtable[route[i - 1]]

    return route