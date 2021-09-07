from random import randint


def make_range_shorter(nums, idx, mini, maxi):
    while mini in nums and nums.index(mini) in idx or mini not in nums:
        if nums.count(mini) > 0:
            cn = 0
            for i in range(len(nums)):
                if nums[i] == mini and i in idx:
                    cn += 1
                else:
                    break
            if cn == nums.count(mini):
                mini += 1
            else:
                break
        else:
            mini += 1
    while maxi in nums and nums.index(maxi) in idx or maxi not in nums:
        if nums.count(maxi) > 0:
            cn = 0
            for i in range(len(nums)):
                if nums[i] == maxi and i in idx:
                    cn += 1
                else:
                    break
            if cn == nums.count(maxi):
                maxi -= 1
            else:
                break
        else:
            maxi -= 1
    return mini, maxi


def take_elements(k):
    in_l = [int(m) for m in '1 2 3 4 5 6 7 8 9'.split()]
    minimal, maximal = min(in_l), max(in_l)
    out_l, idx_l  = [], []
    steps = 0
    if 0 < k <= len(in_l):
        cnt = 0
        while cnt < k:
            e = randint(minimal, maximal)
            steps += 1
            if e in in_l:
                if in_l.index(e) not in idx_l:
                    out_l.append(e)
                    idx_l.append(in_l.index(e))
                    cnt += 1
                elif in_l.count(e) > 1:
                    tmp_cnt = in_l.count(e)
                    tmp_idx = in_l.index(e) + 1
                    for j in range(tmp_cnt):
                        if (in_l[tmp_idx:].index(e) - tmp_idx) not in idx_l:
                            out_l.append(e)
                            idx_l.append(in_l[tmp_idx:].index(e))
                            cnt += 1
                            break
                        else:
                            tmp_idx = in_l[tmp_idx:].index(e)
            minimal, maximal = make_range_shorter(in_l, idx_l, minimal, maximal)
        print('List:', out_l, k, 'elems takes in', steps, 'steps.')
    else:
        print('Invalid request')


for i in range(1, 10):
    take_elements(i)
print('Complete.')