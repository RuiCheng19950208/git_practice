class Solution(object):
    def fizzBuzz(self, n):
        ans=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans.append('FizzBuzz')
            elif i%3!=0 and i%5==0:
                ans.append('Buzz')
            elif i%3==0 and i%5!=0:
                ans.append('Fizz')
            elif i%3!=0 and i%5!=0:
                ans.append(str(i))
        return ans




print(Solution().fizzBuzz(15))