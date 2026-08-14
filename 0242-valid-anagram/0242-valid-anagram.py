class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for ele in s:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1

        for ele in t:
            if ele in dict2:
                dict2[ele] = dict2[ele] + 1
            else:
                dict2[ele] = 1

        if dict1 == dict2:
            return True
        else:
            return False