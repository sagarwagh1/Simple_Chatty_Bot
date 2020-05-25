"""
Find the youngest person among Jack, Alex, Lana and print this person's age.
Sample Input:
23
42
34
Sample Output:
23
"""
# put your python code here

jack_age = int(input())
alex_age = int(input())
lana_age = int(input())
print(min(jack_age, alex_age, lana_age))