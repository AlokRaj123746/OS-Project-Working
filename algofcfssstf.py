def fcfs(requests, head):
    order = [head] + requests
    total = sum(abs(order[i] - order[i - 1]) for i in range(1, len(order)))
    return order, total

def sstf(requests, head):
    reqs = requests.copy()
    order = [head]
    current = head

    while reqs:
        nearest = min(reqs, key=lambda x: abs(x - current))
        order.append(nearest)
        reqs.remove(nearest)
        current = nearest
    
    total = sum(abs(order[i] - order[i - 1]) for i in range(1, len(order)))
    return order, total
