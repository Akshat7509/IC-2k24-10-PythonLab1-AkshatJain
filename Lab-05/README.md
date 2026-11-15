Akshat Jain Ic-2k24-10

Naive vs Optimized Algorithms

Three problems solved twice: first with a simple brute-force method, then with a faster one. Each version is timed so the difference is easy to see.

Requirements
Python 3
Jupyter Notebook or Google Colab
Run a notebook

Open a terminal in this folder and start Jupyter:

powershell
pip install notebook
jupyter notebook

Then open a .ipynb file and choose Run All. You can also upload the notebooks to Google Colab.

Problems
Notebook	Problem	Naive approach	Faster approach
Section_B_Problem_1,_Sum_of_All_Primes_Below_N.ipynb	Sum of all primes below N	Test every divisor up to x	Test divisors up to √x (skipping even numbers), then the Sieve of Eratosthenes
Section_C_Problem_2,_Count_Pairs_With_a_Given_Sum.ipynb	Count pairs that add up to a target	Two nested loops	One pass with a dictionary of seen numbers
Section_D_Problem_3,_K_th_Smallest_Pairwise_Sum_.ipynb	Find the k-th smallest pairwise sum	Build every pair sum and sort	Binary search on the answer with a two-pointer count
How the speed-ups work
Sieve: marks multiples of each prime as not prime, so no number is tested one by one.
Dictionary lookup: for each number, checking whether target - x was already seen takes O(1), so the whole pass is O(N) instead of O(N²).
Binary search on the answer: instead of listing all sums, it guesses a value and counts how many pair sums are at or below it.
Notes
Times are measured with time.time(), so they change from run to run and between computers.
The prime-sum notebook checks small cases (10, 30, 100, 1000) and prints PASS or FAIL before timing.
Small code tweaks only change speed by a constant factor. A better algorithm changes how the time grows with N.
