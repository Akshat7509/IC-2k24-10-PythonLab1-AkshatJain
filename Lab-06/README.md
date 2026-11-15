Akshat Jain Ic-2k24-10

Python Dictionaries

Five small menu-driven programs that use dictionaries to store and report on data, plus a code-tracing section and a theory section.

Requirements
Python 3
Run a program

Open a terminal in this folder and run one of the following commands:

powershell
python pythonLabQ1.py
python pythonLabQ2.py
python pythonLabQ3.py
python pythonLabQ4.py
python pythonLabQ5.py

Q1, Q2, Q3 and Q5 show a numbered menu and keep running until you choose Exit. Q4 asks for one paragraph, prints its analysis and stops.

Programs
File	Program	What it does
pythonLabQ1.py	Student records	Add, update, delete and view students; reports for averages, topper, subject toppers, marks below 40 and grades
pythonLabQ2.py	Employee payroll	Add, update, delete and search employees; payroll per department, top earner per department, salary ranking, 10% raise preview
pythonLabQ3.py	Library lending	Add, issue, return and search books; max 2 books per member; reports for author, multi-book members, out of stock and never issued
pythonLabQ4.py	Word counter	Word counts, top N words, words used once, words grouped by frequency and by length, word search
pythonLabQ5.py	Contact book	10-digit unique phone numbers, several numbers per contact, partial name search, reverse lookup, city grouping
Other files
File	Contents
SectionB.txt	Output and explanation for 8 dictionary snippets
SectionC.txt	Short theory answers on copying, hashing, get(), update() and lookup speed
How the programs work
Records are stored in nested dictionaries, such as {"101": {"name": "...", "marks": {"math": 88}}}.
pop(key, None) deletes safely without a KeyError.
setdefault() and get(key, 0) + 1 handle grouping and counting.
Dictionary comprehensions build reports and the Q5 {phone: name} reverse lookup.
sorted() with a lambda key handles ranking and sorting.
Notes
Data is kept in memory only, so it is lost when a program exits.
Entering text where a number is expected in Q1 raises a ValueError.
