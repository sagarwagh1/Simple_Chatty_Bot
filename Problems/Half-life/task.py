"""
In nuclear physics, the half-life is used to describe the rate with which elements undergo radioactive decay.
More precisely, it is the time required for an element to reduce in half.
Let's take an isotope of Radium (Ra) called radium-223. Say, its half-life is about 12 days.
This means that every 12 days the number of atoms reduces in half.
Write a program that calculates how many full half-life periods (in days) it would take for a certain amount of
radium-223 to reduce to a specific value.

The input format:
The first line with the starting amount of atoms N (from 2 to 1,000,000), the second line with the resulting quantity R.
The output format:
The number of full half-life periods (in days) T it would take for radium-223 to reduce from N to R.

Assume that any change would take at least 1 half-life period.
Suppose, the initial number of atoms is 4 and the resulting quantity equals to 3. In 12 days,
the number will reduce to 2 atoms. Since we are counting full half-life periods, you should write 12 and so on.

Sample Input:
4
3
Sample Output:
12

Sample Input:
835950
139505
Sample Output:
36
"""
# put your python code here

N = int(input())
R = int(input())
T = 0
while N > R:
    T += 12
    N = N // 2
print(T)