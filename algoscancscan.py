def scan(requests, head, disk_size=200, direction="right"):
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    order = [head]

    if direction == "right":
        # Move right → end → reverse to left
        order += right + [disk_size - 1] + left[::-1]
    else:
        # Move left → start → reverse to right
        order += left[::-1] + [0] + right

    total = sum(abs(order[i] - order[i - 1]) for i in range(1, len(order)))
    return order, total


def c_scan(requests, head, disk_size=200, direction="right"):
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    if direction == "right":   # Clockwise →
        order = [head] + right + [disk_size - 1, 0] + left
    else:                      # Anti-Clockwise ←
        order = [head] + left[::-1] + [0, disk_size - 1] + right[::-1]

    total = sum(abs(order[i] - order[i - 1]) for i in range(1, len(order)))
    return order, total