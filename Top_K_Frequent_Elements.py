def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # we have a list of lists
    # each index represents how many times a number has shown up
    count = {}
    freq = [[] for i in range(len(nums))]
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


list1 = [1, 1, 1, 2, 2, 3]

print(top_k_frequent(list1, 2))
