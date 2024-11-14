from functools import reduce


def update_state(old_state, n):
    new_state = {}
    for i in range(n):
        for j in range(n):
            # basically we should be multiplying by 4 here.
            left_i = max(i - 1, 0)
            right_i = min(i + 1, n - 1)
            left_j = max(j - 1, 0)
            right_j = min(j + 1, n - 1)

            new_state[(i, j)] = old_state[(left_i, left_j)] + old_state[(left_i, right_j)] + old_state[(right_i, left_j)] + old_state[(right_i, right_j)]
    
    return new_state


def reduce_frac(a , b):
    if a == 0:
        return 0, 1
    orig_a = a
    orig_b = b
    while b != 0:
        t = b
        b = a % b
        a = t
    return orig_a // a, orig_b // a


def solve(n, x, y, d):
    x = x - 1 
    y = y - 1  # they use 1 based indexing
    d = d+ 1

    # states is a look up of nxn
    states = {}
    for i in range(n):
        for j in range(n):
            states[(i, j)] = 0

    states[(x, y)] = 1

    denom = 1
    final_denom = 1
    for i in range(d):
        final_denom = 4*final_denom
    denoms = []
    nums = []
    for day in range(0, d ):
        num_sum = 0
        for i in range(n):
            # count all the bears who have slept together.
            # they shouldnt count again though...
            num_sum += states[(i, i)]
            states[(i, i)] = 0

        nums.append(num_sum  * final_denom)

        states = update_state(states, n)   
        denoms.append(denom)

        final_denom //= 4
        denom*=4
    
    # the total at the end, is denom
    # but we have to count each num based on how much is left
    ans_n, ans_d = reduce_frac(sum(nums), denom)
    return f"{ans_n}/{ans_d}"


n, x, y, d = map(int, input().split(" "))
print(solve(n, x, y, d))


