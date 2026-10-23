from collections import deque


def shortest_path(board_size, jumps):
    """Return minimum throws and a shortest path using BFS."""
    if board_size < 2:
        return 0, [1]

    distances = [-1] * (board_size + 1)
    parent = [None] * (board_size + 1)
    distances[1] = 0
    queue = deque([1])

    while queue:
        square = queue.popleft()
        if square == board_size:
            break

        for dice in range(1, 7):
            next_square = square + dice
            if next_square > board_size:
                break

            destination = jumps.get(next_square, next_square)
            if distances[destination] == -1:
                distances[destination] = distances[square] + 1
                parent[destination] = square
                queue.append(destination)

    if distances[board_size] == -1:
        return -1, []

    path = []
    current = board_size
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return distances[board_size], path


def main():
    board_size = 30
    # Map each snake/ladder start square to its destination.
    jumps = {
        3: 22,   # Ladder
        5: 8,    # Ladder
        11: 26,  # Ladder
        20: 29,  # Ladder
        27: 1,   # Snake
        21: 9,   # Snake
        17: 4,   # Snake
        19: 7    # Snake
    }

    print("--- Snake and Ladder Using BFS ---")
    print("Board squares: 1 to", board_size)
    print("Snakes and ladders:")
    for start, end in sorted(jumps.items()):
        kind = "Ladder" if end > start else "Snake"
        print(f"{kind}: {start} -> {end}")

    throws, path = shortest_path(board_size, jumps)
    if throws == -1:
        print("\nThe final square cannot be reached.")
    else:
        print("\nMinimum dice throws required:", throws)
        print("BFS path:", " -> ".join(map(str, path)))
        print("Each BFS edge represents one dice throw.")
        print("The path shows squares after applying snakes/ladders.")


if __name__ == "__main__":
    main()
