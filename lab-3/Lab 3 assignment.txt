Activity: Find the Time and Space Complexity
For each snippet, write the time complexity and space complexity using Big-O notation, and justify your answer in one line.


Snippet 1
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val


Time complexity: ____O(n)___________ Space complexity: ________O(1)_______ Justify:
Time: O(n) - n-1 comparisons.Space: O(1) - only max_val + loop variable.


Snippet 2
def has_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


Time complexity: _____O(n²)__________ Space complexity: _____O(1)__________ Justify:
Time: O(n²) - sum_{i=0}^{n-1} (n-i-1) = n(n-1)/2 comparisons.Space: O(1) - no extra data structures, just i,j.


Snippet 3
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
Time complexity: ____ O(log n)___________ Space complexity: ________O(log n)____ Justify:
*Time: O(log₁₀ n)* - one call per digit, d = number of digits.
*Space: O(log₁₀ n)* - recursion depth = d.
Snippet 4
def print_pairs(arr):
    n = len(arr)
    result = []
    for i in range(n):
        for j in range(n):
            result.append((arr[i], arr[j]))
    return result


Time complexity: ____O(n²)___________ Space complexity: ______O(n²)_________ Justify:Time: O(n²) - n*n iterations.Space: O(n²) - stores n² pairs in result.


Snippet 5
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


Time complexity: ____O(log n)___________ Space complexity: _____O(1)__________ Justify: Time: O(log n) - halves search space each iteration.Space: O(1) - iterative, only 3 vars.


Snippet 6
def matrix_multiply(a, b):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
    return result


Time complexity: ______O(n³)_________ Space complexity: _____O(n²)__________ Justify:Correct.
*Time: O(n³)* - 3 nested loops of n.
*Space: O(n²)* - n x n result matrix.


Snippet 7
def to_sparse(matrix):
    triples = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                triples.append((r, c, matrix[r][c]))
    return triples


Time complexity (in terms of matrix dimensions m and n): ___O(m _ n)____________ Space complexity (in terms of k non-zero elements): ____O(k)___________ Justify:
Time: O(m * n) - visits every cell.Space: O(k) - k = non-zero count, stores one triple per.


Snippet 8
def process(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])
    for j in range(n):
        for k in range(n):
            print(arr[j], arr[k])


Time complexity: _____O(n²)__________ Justify:


Snippet 9
def check_first_ten(arr):
    for i in range(len(arr)):
        for j in range(10):
            if arr[i] == j:
                return True
    return False


Time complexity: ___O(n²)____________ Justify: Inner loop is range(10) = constant 10, not n.So n * 10 = 10n = O(n).


Snippet 10
def reverse_new(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr


Time complexity: ____O(n)___________ Space complexity: ______O(n)_________ Justify:
Time: O(n) - single pass over n elements.
Space: O(n) - creates new array of size n.
Snippet 11
def reverse_in_place(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


Time complexity: ____O(n)___________ Space complexity: ______O(1)_________ Justify:Time: O(n) - swaps n/2 times.Space: O(1) - in-place, no extra array.


Snippet 12
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


Time complexity: ____O(n)___________ Space complexity: ______O(n)_________ Justify:
Time: O(n) - n recursive calls.Space: O(n) - recursion stack depth n


Snippet 13
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


Time complexity: ____O(2^n)___________ Space complexity: _____O(n)__________ Justify: Time: O(2^n) - calls double each level.Space: O(n) - deepest stack is n


Snippet 14
def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0
    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count


Time complexity: ____O(n)___________ Space complexity: ______O(n)_________ Justify:


Snippet 15
def print_all_subsets(arr):
    n = len(arr)
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        print(subset)


Time complexity: _______________ Justify:Time: O(n) - single pass, set lookup O(1).Space: O(n) - stores up to n elements in seen


Snippet 16
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


Time complexity: ______O(n)_________ Space complexity: ______O(n)_________ Justify:Time:  - single pass, set lookup O(1).Space:  - stores up to n elements in seen
Snippet 17
def is_palindrome(s):
    return s == s[::-1]


Time complexity: ______ O(n)_________ Space complexity: ______O(n) _________ Justify:
Time: - slicing copies n chars + compare n.Space: - s[::-1] creates new string of size n.
Snippet 18
def flatten(matrix):
    flat = []
    for row in matrix:
        for val in row:
            flat.append(val)
    return flat


Time complexity (in terms of m rows and n columns): _______O(m_n)________ Space complexity: ______O(m_n)_________ Justify:
Time:  - visits each of m_n elements once.Space:  - stores all m_n elements in new list flat
Snippet 19
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)
Time complexity: ______O(exp)_________ Space complexity: ______O(exp)_________ Justify:
Time:  - exp recursive calls.Space:  - recursion depth exp
Snippet 20
def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    return half * half * base


Time complexity: ________O(log exp)_______ Space complexity: _____O(log exp)__________ Justify:
Time:  - exp halves each call.Space:  - recursion depth log exp.
Snippet 21
def has_common_element(a, b):
    for x in a:
        for y in b:
            if x == y:
                return True
    return False


Time complexity (in terms of the sizes of a and b): _______ O(|a| * |b|)________ Space complexity: ______ O(1)_________ 
Time: - nested loops check all pairs.Space: - no extra structure, just 2 variables
Snippet 22
def build_frequency_map(arr):
    freq = {}
    for val in arr:
        freq[val] = freq.get(val, 0) + 1
    return freq


Time complexity: ______O(n)_________ Space complexity: _____O(n)__________ Justify:
Time:  - single pass, dict ops O(1).Space:  - worst case n distinct keys, O(k) where k = distinct count