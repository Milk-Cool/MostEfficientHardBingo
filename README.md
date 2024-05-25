# MostEfficientHardBingo
Trying to prove that my suggested method is the most efficient for creating a hard bingo

# Updates
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