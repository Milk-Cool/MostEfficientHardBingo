# MostEfficientHardBingo
Trying to prove that my suggested method is the most efficient for creating a hard bingo

# Updates
## May 25th, ~15:53 MSK
I fixed three bugs in my program. Now it outputs 20 bingos.\
I know for sure that these combinations are the most efficient, because I've been using a score system. Basically:
1. For each cell, you calculate how many cells are in its row, column and diagonals;
2. Then you add the values from all marked cells;
3. Then you select the bingos with the **least** score;
4. And output these bingos.

These bingos should also meet the criterion saying that for each row, column and diagonal there should be **exactly one** marked cell.\
To run my program and only get the bingos that meet the criteria:
```bash
python3 main.py > out.log
grep -n -F 'combinations found for' out.log
cat out.log | tail -n +33605 > out_final.log
cat out_final.log
```
> Please note that `33605` may be a different number if you modify the program. It's the last line number from the output from `grep`.

The output is gonna be the bingo with a number in each cell saying how often it appears in a row, a column, or a diagonal.\
I guess you could say that my bingo is still the most efficient one because there's a cell with a weight of 4, in which you can put the hardest to check thing. Though, there are two more bingos that meet the same criterion:
||||▮▮||
|-|-|-|-|-|
|▮▮|||||
|||▮▮|||
|||||▮▮|
||▮▮||||

||▮▮||||
|-|-|-|-|-|
|||||▮▮|
|||▮▮|||
|▮▮|||||
||||▮▮||

Though I still think that mine is better because it's easier to remember... or it's just that I want my point to be proven :)\
*And... I guess that's it! It's been a fun journey. :)*

## May 25th, ~15:21 MSK
I improved my program once again, this time it excludes the repeating combinations. It takes roughly 3 minutes to complete on my laptop. I'm pretty close – it only shows 45 "valid" combinations now. Some of them are actually invalid because they don't have a single square on a diagonal so I'll have to do a bit more coding.

## May 25th, ~15:00 MSK
I rewrote another part, and most combinations still don't meet my criteria. I'll review them and rewrite the program again.\
I've also added out.log and out_final.log to .gitignore for storing results.

## May 25th, ~14:43 MSK
I rewrote a certain part of the program and also added type annotations. (I kinda wish there were typedef's in Python...) It now outputs invalid combinations, I'll try rewriting it again :(

## May 25th, ~14:23 MSK
So... it didn't find anything. I'll try fixing it. Also, I thought it would take longer.\
**EDIT**: longer to execute*

## May 25th, ~14:22 MSK
I wrote the program. You can check it out in the `main.py` file. It takes a while to execute. I wonder if I can optimise it. Also, it didn't actually take that long for me to write it - I took a break :)

## May 25th, ~12:56 MSK
I think I found the most efficient way to make a hard bingo?
It looks something like this:
||▮▮||||
|-|-|-|-|-|
|▮▮|||||
|||▮▮|||
|||||▮▮|
||||▮▮||

Or like this:
||||▮▮||
|-|-|-|-|-|
|||||▮▮|
|||▮▮|||
|▮▮|||||
||▮▮||||

I think that it is the mosty efficient because it covers all of the combinations (all rows, columns and diagonals) with the least amount of squares.\
It works like this: you put the hardest to check square in the middle becuase it covers a row, a column and both diagonals at the same time, and the four next hardest to check squares in the other four marked squares because each covers a row and a column. I think that this is the most efficient way to cover all rows, columns and diagonals since there are no marked squares that cover a row or a column that was covered by another marked square.\
I'll try proving that it is the most efficient way with a Python program. Or maybe I'll find a new way that is as efficient as this one or even more efficient. Who knows :)