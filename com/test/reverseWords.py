class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        k = s.strip().split(" ")
        returnWords = ""
        for word in k[::-1]:
            if word != "" and word != " ":
                returnWords += word + " "
        return returnWords.strip()

x= Solution().reverseWords("rahan akbar ali mohamed ibrahim")
print(x)