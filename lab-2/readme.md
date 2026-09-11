Akshat Jain Ic-2k24-10
# Python Star Patterns

A small collection of beginner-friendly Python programs that print star (`*`) patterns in the terminal. Each program asks for the number of rows, then displays its pattern.

## Requirements

- Python 3

## Run a program

Open a terminal in this folder and run one of the following commands:

```powershell
python traiangle.py
python sqaure.py
python Right_traiangle.py
python inverse_triangle.py
python rhombus.py
```

> The filenames `traiangle.py` and `sqaure.py` contain spelling mistakes, but the commands above use the current filenames exactly.

When prompted, enter a positive whole number, for example `5`.

## Programs

| File | Pattern printed | Example with 5 rows |
| --- | --- | --- |
| `traiangle.py` | Centered pyramid triangle | `    *`<br>`   ***`<br>`  *****`<br>` *******`<br>`*********` |
| `sqaure.py` | Solid square | `* * * * *` repeated for 5 rows |
| `Right_traiangle.py` | Left-aligned right triangle | `*`<br>`* *`<br>`* * *`<br>`* * * *`<br>`* * * * *` |
| `inverse_triangle.py` | Inverted left-aligned right triangle | `* * * * *`<br>`* * * *`<br>`* * *`<br>`* *`<br>`*` |
| `rhombus.py` | Slanted rhombus/parallelogram | Five rows of stars, indented less on every next row |

## How the patterns work

All programs use `for` loops:

- `range(1, n + 1)` counts upward to build patterns from top to bottom.
- `range(n, 0, -1)` counts backward to create the inverted triangle.
- Multiplying strings, such as `"* " * i`, repeats stars without another nested loop.
- Leading spaces, such as `" " * (n - i)`, position the centered triangle and rhombus.

## Notes

- Entering `0` or a negative number produces no visible pattern.
- Entering text instead of a whole number raises a `ValueError` because the programs use `int(input(...))`.
- These programs print output only; they do not save files or modify data.
