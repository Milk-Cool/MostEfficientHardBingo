# v2

import copy


BINGO_SIZE = 5
MAX_COUNT = 5

min_acnt = float("inf")
min_stats_bingos: list[tuple[tuple[list[int],
                                   list[int], list[int]], list[list[bool]]]] = []
results: list[tuple[int, int | float, list[tuple[tuple[list[int],
                                                       list[int], list[int]], list[list[bool]]]]]] = []


def stat_bingo(bingo: list[list[bool]]) -> tuple[list[int], list[int], list[int]]:
    rows_covered = [0 for _ in range(BINGO_SIZE)]
    columns_covered = [0 for _ in range(BINGO_SIZE)]
    diagonals_covered = [0 for _ in range(2)]

    for x in range(BINGO_SIZE):
        for y in range(BINGO_SIZE):
            if not bingo[x][y]:
                continue
            if x - y == 0:
                diagonals_covered[0] += 1
            if y - x == 0:
                diagonals_covered[1] += 1
            columns_covered[x] += 1
            rows_covered[y] += 1

    return rows_covered, columns_covered, diagonals_covered


def print_stats(stats: tuple[list[int], list[int], list[int]], bingo: list[list[bool]]) -> int:
    rows_covered, columns_covered, diagonals_covered = stats
    acnt = 0
    for x in range(BINGO_SIZE):
        print("-" * (BINGO_SIZE * 2 + 1))
        for y in range(BINGO_SIZE):
            print("|\x1b[37m", end="")
            # green if marked else red
            print("\x1b[42m" if bingo[x][y] else "\x1b[41m", end="")
            cnt = columns_covered[x] + rows_covered[y]
            acnt += cnt
            if x - y == 0:
                cnt += diagonals_covered[0]
            elif y - x == 0:
                cnt += diagonals_covered[1]
            print(str(cnt), end="")
            print("\x1b[0m", end="")
        print("|")
    print("-" * (BINGO_SIZE * 2 + 1))
    return acnt


def bingo_callback(stats: tuple[list[int], list[int], list[int]], bingo: list[list[bool]]):
    global min_acnt, min_stats_bingos
    acnt = print_stats(stats, bingo)
    if acnt < min_acnt:
        min_stats_bingos = []
        min_acnt = acnt  # the new king
    if acnt == min_acnt:
        min_stats_bingos += [(stats, bingo)]


def recurse_bingos(depth, bingo: list[list[bool]], checker, cb):
    if depth == 0:
        stats = stat_bingo(bingo)
        if checker(stats, bingo):
            cb(stats, bingo)
        return
    for x in range(BINGO_SIZE):
        for y in range(BINGO_SIZE):
            if not bingo[x][y]:
                bingo_clone = copy.deepcopy(bingo)
                bingo_clone[x][y] = True
                recurse_bingos(depth - 1, bingo_clone, checker, cb)


def check_bingo(stats: tuple[list[int], list[int], list[int]], bingo: list[list[bool]]):
    rows_covered, columns_covered, diagonals_covered = stats
    cnt = 0
    
    for x in range(BINGO_SIZE):
        if columns_covered[x] != 1:
            return False
    for y in range(BINGO_SIZE):
        if rows_covered[y] != 1:
            return False
    for i in range(2):
        if diagonals_covered[i] != 1:
            return False
    
    for x in range(BINGO_SIZE):
        for y in range(BINGO_SIZE):
            if bingo[x][y]:
                cnt += 1
    if cnt > MAX_COUNT:
        return False

    return True


def main():
    global min_acnt, min_stats_bingos, results
    # marked cells count
    for i in range(1, MAX_COUNT + 1):
        min_acnt = float("inf")
        min_stats_bingos = []

        bingo = [[False for _y in range(BINGO_SIZE)]
                 for _x in range(BINGO_SIZE)]
        recurse_bingos(i, bingo, check_bingo, bingo_callback)
        results += [(i, min_acnt, min_stats_bingos)]
    for result in results:
        print(result[1], "combinations found for", result[0], "marked cells")
        for stat_bingo in result[2]:
            print_stats(stat_bingo[0], stat_bingo[1])


if __name__ == "__main__":
    main()
