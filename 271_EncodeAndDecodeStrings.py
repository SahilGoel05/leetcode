class Solution:

    '''
    ["neet","code","love","you"]

    encode:
    r_h = "4:4:4:4:3:"
    r_s = "neetcodeloveyou"
    r = "10:4:4:4:4:3:neetcodeloveyou"

    decode:
    result = ["neet", "code", ]
    header_len = 10
    num_strs = 4
    strs = "you"
    str_len = 4
    s = "4:3:neetcodeloveyou"
    
    '''
    def encode(self, strs: List[str]) -> str:
        num_strs = len(strs)
        result_header = str(num_strs) + ":"
        result_strings = ""
        for string in strs:
            result_header += str(len(string)) + ":"
            result_strings += string
        return str(len(result_header)) + ":" + result_header + result_strings

    def decode(self, s: str) -> List[str]:
        result = []
        header_len = int(s[:s.find(":")])
        s = s[s.find(":") + 1:]
        num_strs = int(s[:s.find(":")])
        strs = s[header_len:]
        s = s[s.find(":") + 1:]
        for i in range(num_strs):
            str_len = int(s[:s.find(":")])
            s = s[s.find(":") + 1:]
            result.append(strs[:str_len])
            strs = strs[str_len:]
        return result

'''
Optimal Solution:

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

TC: O(m)
SC: O(m+n)
'''

            

