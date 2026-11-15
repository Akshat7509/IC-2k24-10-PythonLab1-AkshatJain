Akshat Jain Ic-2k24-10

Sum of Primes with Timing

A small Python program that finds all prime numbers up to N, adds them up, and shows how long the calculation took.

Requirements
Python 3
Run the program

Open a terminal in this folder and run:

powershell
python assignment.py

When prompted, enter a positive whole number, for example 10.

Example
text
enter the number til which you want to sum the primes10
Sum of primes: 17
Time taken: 0.0 seconds

Primes up to 10 are 2, 3, 5 and 7, which add up to 17. The time shown will vary on every run and computer.

Program
File	What it does
assignment.py	Checks every number from 2 to N, collects the primes in a list, then prints their sum and the time taken
How it works
For each number i, it only tries divisors from 2 up to int(i ** 0.5). If a number has a factor, one factor is always at most its square root.
break stops checking a number as soon as a divisor is found.
time.time() is read before and after the loop, and the difference is the time taken.
Notes
The sum includes N itself if N is prime.
This method gets slower as N grows. Lab 5 compares it with faster approaches such as the Sieve of Eratosthenes.
Entering text instead of a whole number raises a ValueError.
