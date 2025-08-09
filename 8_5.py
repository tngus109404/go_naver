#백준_10828
import sys
input = lambda: sys.stdin.readline().strip()
stack=[]
def push(X): stack.append(X)
def pop(): print(stack.pop() if stack else -1)
def size(): print(len(stack))
def empty() : print(0 if queue else 1)
def top(): print(stack[-1] if stack else -1)
commands = {
    "pop" : pop,
    "size" : size,
    "empty" : empty,
    "top" : top
}
N = int(input())
for _ in range(N):
    parts = input().split()
    if parts[0] == "push":
        push(parts[1])
    else:
        commands[parts[0]]()


#백준_10845
from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
queue=deque([])
def push(X) : queue.append(X)
def pop() : print(queue.popleft() if queue else -1)
def size() : print(len(queue))
def empty() : print(0 if queue else 1)
def front() : print(queue[0] if queue else -1)
def back() : print(queue[-1] if queue else -1)
commands = {
    "pop" : pop,
    "size" : size,
    "empty" : empty,
    "front" : front,
    "back" : back
}
N = int(input())
for _ in range(N):
    parts = input().split()
    if parts[0] == "push":
        push(parts[1])
    else:
        commands[parts[0]]()


#백준_18258
from collections import deque
import sys
input = lambda: sys.stdin.readline().strip()
queue=deque([])
output=[]
def push(X) : queue.append(X)
def pop() : output.append(queue.popleft() if queue else -1)
def size() : output.append(len(queue))
def empty() : output.append(0 if queue else 1)
def front() : output.append(queue[0] if queue else -1)
def back() : output.append(queue[-1] if queue else -1)
commands = {
    "pop" : pop,
    "size" : size,
    "empty" : empty,
    "front" : front,
    "back" : back
}
N = int(input())
for _ in range(N):
    parts = input().split()
    if parts[0] == "push":
        push(parts[1])
    else:
        commands[parts[0]]()


#백준_2164
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()
N = int(input())
queue = deque(range(1,N+1))
while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])


#프로그래머스_기능개발
import math
def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)] #사용법 익힐것!
    prev_day = days[0]
    count = 1
    for current_day in days[1:]:
        if current_day <= prev_day:
            count += 1
        else:
            answer.append(count)
            prev_day = current_day
            count = 1
    answer.append(count)
    return answer
print(solution([93,30,55],[1,30,5])) #[2,1]
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])) # [1,3,2]

#프로그래머스_프린터
from collections import deque
def solution(priorities, location):
    queue = deque((p,i) for i, p in enumerate(priorities))
    count = 0
    while queue:
        p,i = queue.popleft()
        if any(p < q[0] for q in queue):
            queue.append((p,i))
        else:
            count +=1
            if i == location:
                return count
print(solution([2,1,3,2], 2)) #1
print(solution([1,1,9,1,1,1], 0)) #5

#프로그래머스_더맵게
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second * 2))
        count += 1
    return count if scoville[0] >= K else -1
print(solution([1, 2, 3, 9, 10, 12],7)) # 2