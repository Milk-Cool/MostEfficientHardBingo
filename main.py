# v1

import copy


BINGO_SIZE = 5
MAX_COUNT = 5


def stat_bingo(bingo: list[list[bool]]):
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


def print_stats(stats, bingo: list[list[bool]]):
    rows_covered, columns_covered, diagonals_covered = stats
    for x in range(BINGO_SIZE):
        print("-" * (BINGO_SIZE * 2 + 1))
        for y in range(BINGO_SIZE):
            print("|\x1b[37m", end="")
            # green if marked else red
            print("\x1b[42m" if bingo[x][y] else "\x1b[41m", end="")
            cnt = columns_covered[x] + rows_covered[y]
            if x - y == 0:
                cnt += diagonals_covered[0]
            elif y - x == 0:
                cnt += diagonals_covered[1]
            print(str(cnt), end="")
            print("\x1b[0m", end="")
        print("|")
    print("-" * (BINGO_SIZE * 2 + 1))


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


def check_bingo(stats, bingo: list[list[bool]]):
    rows_covered, columns_covered, diagonals_covered = stats
    cnt = 0
    for x in range(BINGO_SIZE):
        for y in range(BINGO_SIZE):
            if bingo[x][y]:
                scnt = rows_covered[y] + columns_covered[x]
                if x - y == 0:
                    scnt += diagonals_covered[0]
                if y - x == 0:
                    scnt += diagonals_covered[1]
                if scnt != 1:
                    return False
                cnt += 1
    if cnt > MAX_COUNT:
        return False

    return True


def main():
    # marked cells count
    for i in range(1, MAX_COUNT + 1):
        bingo = [[False for _y in range(BINGO_SIZE)]
                 for _x in range(BINGO_SIZE)]
        recurse_bingos(i, bingo, check_bingo, print_stats)


if __name__ == "__main__":
    main()
