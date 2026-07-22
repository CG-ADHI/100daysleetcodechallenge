class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         res = defaultdict(list)  # Dictionary to store groups of anagrams

         for s in strs:
            count = [0] * 26  # Frequency array for letters a-z

            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

         return list(res.values())