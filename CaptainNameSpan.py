import re
Captains = open('C:\Manjunath\Personal\Manju\pi\Captains.txt', 'r').read()
SplitCaptain = Captains.split('\n')

def FunctionToGetSpanCaptainName(SplitCaptain):
    for name in SplitCaptain:
        splitname=name.split(',')
        matchObj = re.match("^Player", name)
        if len(splitname)>2 and not matchObj:
            print ("Captain:"+splitname[0]+", Span:"+splitname[1])
            

FunctionToGetSpanCaptainName(SplitCaptain)
