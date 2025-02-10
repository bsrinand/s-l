from collections import deque

def min_dice_throws(board):
    n = len(board)
    visited = [False] * n
    queue = deque([(0, 0)])  # (index, dice rolls)

    while queue:
        index, rolls = queue.popleft()
        if index == n - 1:
            return rolls

        for dice in range(1, 7):
            next_pos = index + dice
            if next_pos < n and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((board[next_pos] if board[next_pos] != -1 else next_pos, rolls + 1))

    return -1

board = [-1] * 30
board[2], board[21] = 21, 9  # Ladders
board[16], board[28] = 6, 0  # Snakes
print(min_dice_throws(board))  # Example Output: 4
