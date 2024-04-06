def kidsWithCandies(candies, extraCandies):
    result = []         #Initializing the array 'result[]'
    for i in range(len(candies)):   #Iterate through al elemnets in the array
        if candies[i]+extraCandies >= max(candies): #Check the condition of >= candies
            result.append(True)                     #Append TRUE in result[]
        else:
            result.append(False)                    #Append FALSE in result[]
    #return result          #Use this for leetcode
    print(result)           #Use this for your own testing e.g VsCode

kidsWithCandies([12,1,12],10)   #Testcase with expected output of [True, False, True]