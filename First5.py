'''
Print First5 Captains names
'''
import re 

def FunctionToGetCaptainsName(SplitCaptain):
    count=0
    CaptainName=[]
    for name in SplitCaptain:
        if count==5:
            break
        matchObj = re.match("^Player", name)
        if not matchObj:
            splitname= name.split(',')
            CaptainName.append(splitname[0])
            count+=1
    return CaptainName
    
Captains = open('C:\Manjunath\Personal\Manju\pi\Captains.txt', 'r').read()
SplitCaptain = Captains.split('\n')

print(FunctionToGetCaptainsName(SplitCaptain))
