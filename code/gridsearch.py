# Link to challenge: https://www.hackerrank.com/challenges/the-grid-search

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def gets():
    return sys.stdin.readline()

def read_mat():
    dim = gets().split()
    m, n = dim
    m = int(m)
    mat = []
    for i in xrange(m):
        arr = (' '.join(gets())).split()
        mat.append([int(j) for j in arr])
    return mat

def check_pat(p, g):
    print p, g
    return

n = int(gets())
for i in xrange(n):
    g = read_mat()
    p = read_mat()
    check_pat(p, g)
        