def twoSum( nums, target):
     
    numsdict = {value: index for index, value in enumerate(nums)}

    for i in range(target + 1):
        if i - 1 in numsdict and (target - i - 1) in numsdict:
            if i - 1 == target - i - 1:
                return [nums.index(i), numsdict[target - i]]
            return [numsdict[i], numsdict[target - i]]
    
    # if target == 0 and 0 in numsdict:
    #     return [nums.index(0), numsdict[target]]

nums = [-3,4,3,90]
target = 0

print(twoSum(nums, target))