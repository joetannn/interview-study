class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1 ()
        # 2 ()() (())
        #3 ()()() (())() ()(()) ((())) (()())


        # 2 -> 1 (generate) / generate
        # ()() (()) 3 -> 2 (g)(g)g (g(g))g 

        retArr = ["()"]
        for i in range(1, n):
            tempMap = set()
            for prev in retArr:
                tempMap.add(prev + "()")
                for c in range(len(prev)):
                    if prev[c] == "(":
                        newStr = prev[:c + 1] + "()" + prev[c + 1:]
                        if newStr not in tempMap:
                            tempMap.add(newStr)


            retArr = list(tempMap)

        




        


        return retArr
                


        