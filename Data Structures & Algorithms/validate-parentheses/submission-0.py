class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        key = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in key:
                if st and st[-1] == key[c]:
                    st.pop()
                else: return False
            else:
                st.append(c)
        return True if not st else False