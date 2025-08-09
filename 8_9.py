#백준_1463번
import sys
input = lambda: sys.stdin.readline().strip()
N = int(input())
dp = [0] * (N+1)
for i in range(2,N+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i],dp[i//2]+1)    
print(dp[N])


#백준_9095번
import sys
input = lambda: sys.stdin.readline().strip()
T = int(input())
test_case = [int(input()) for _ in range(T)]
dp = [0] * 12
dp[1],dp[2],dp[3] = 1,2,4
for i in range(4,12):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
for d in test_case:
    print(dp[d])


#백준_11726번
import sys
input = lambda: sys.stdin.readline().strip()
N = int(input())
if N < 2:    
    print(N)
    exit()
dp=[0]*(N+1)
dp[1],dp[2] = 1,2
for i in range(3,N+1):
    dp[i]= dp[i-2] + dp[i-1] % 10007
print(dp[N])


#프로그래머스_정수삼각형
def solution(triangle):
    dp=[row[:] for row in triangle]
    for i in range(len(dp)-2,-1,-1):
        for j in range(len(dp[i])):
            dp[i][j] += max(dp[i+1][j],dp[i+1][j+1])
    return dp[0][0]
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # 30   


#프로그래머스_2xN타일링
def solution(n):
    if n < 3:
        return n
    dp=[0]*(n+1)
    dp[0],dp[1],dp[2] = 0,1,2
    for i in range(3,n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[n]
print(solution(4)) # 5   

