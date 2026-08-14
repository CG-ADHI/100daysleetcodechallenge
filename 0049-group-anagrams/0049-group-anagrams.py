class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadict = {}

        for word in strs:
            sortword = "".join(sorted(word))

            if sortword in anadict:
                anadict[sortword].append(word)
            else:
                anadict[sortword] = [word]

        return list(anadict.values())