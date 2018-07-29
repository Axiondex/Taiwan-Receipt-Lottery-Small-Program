from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import re, sys, urllib
import htmlparse
#FileSave() call GrabWebSrc()
#RunNumber() call SplitNumb() call RegexFiliter()
class GetLuck(object):
    def FileSave(self):
        with open("recipthtml.txt","w+") as reciptHtml: #Save html information from GrabWebSrc()
            #call GrabWebSrc function
            reciptHtml.write(self.GrabWebSrc())
            if reciptHtml.closed == False:
                reciptHtml.close()

    def GrabWebSrc(self):
        req = Request('http://invoice.etax.nat.gov.tw/') 
        #grab website information
        try:
            response = urlopen(req)
        except(URLError, e):
            print(e.code())
        page = str(response.read(),'utf8')
        #print (page)
        #print response.info()	
        return page
	
    def RunNumb(self):#Here the user type numbers to see what's the result. 
        #call SplitNumb()
        Ary = self.SplitNumb()
        AryGuest = []
        match, j = 0, 0
        typin = input("Enter the Number")
        while not typin.isdigit():
            typin = input("Please type again")
            s = int(typin)
            guestnumlen = len(typin)
            while s > 0:
                AryGuest.append(s % 10)
                s = s // 10
                if guestnumlen < 8:
                    for x in range(8 - guestnumlen):
                        AryGuest.append(0)
	#AryGuest = AryGuest.reverse()
	#rint AryGuest
	#print Ary
        judge = True
        reward = 0
        for i in Ary[0]:
            if i == -1:
                if match > 2:
                    break
                else:
                    reward += 1
                    match = 0
                    j = 0 #reset number and start from the begining
                    judge = True
            elif i == AryGuest[j] and judge:
                match += 1
                j += 1
            else:
                judge = False

        if match == 8 and reward == 0:
            print ("win the biggest moneny 100 million")
        elif match == 8 and reward == 1:
            print ("win 2 million")
        elif reward >= 2:
            if match == 3:
                print ("win 200")
            elif match == 4:
                print ("win 1000")
            elif match == 5:
                print ("win 4000")
            elif match == 6:
                print ("win 10000")
            elif match == 7:
                print ("win 40000")
            elif match == 8:
                print ("win twenty thousand")
        print (match,reward) 
        
    def SplitNumb(self):#Divid each number to array 
        NumbAry = self.RegexFilter()#call RegexFiliter function
	#print NumbAry
        Ary = []
        NumSplit = [[]for i in range (2)]
        m = 0
        temp = 8
        for line in NumbAry:
            x = re.split('\D+',line) #\u3001 is comma #line.encode('utf-8')
	    #print x
            Ary.append(x)
	    #print Ary
        i = 0
        for i in Ary:
            for j in i:
                numb = int(j)
                #print numb 
                if len(j) != temp and len(j) == 8:
                    #print temp,len(j)
                    m = 1 
                    for i in range(len(j)):
                        NumSplit[m].append(numb % 10)
                        numb = numb // 10
                        NumSplit[m].append(-1)      
                        temp = len(j)
        #[k.split(-1)[0] for k in NumSplit]
	#print NumSplit,
        return NumSplit
	
#Use regular express to take the number on website
#filiter the imformation we need
    def RegexFilter(self): 
        with open("recipthtml.txt","r+") as html:
            #MyItems = pattern.match(html.read())
            #MyItems = re.findall('[\w-]+',html.read())
            page = html.read()
            Unicodepage = page 
            MyItems = re.findall('<span.*?class="t18Red">(.*?)</span>',Unicodepage,re.S)
            #print Unicodepage
            #print page
            items =[]
            month = re.findall('<h2>\d+.*?</h2>',Unicodepage)
            #print (MyItems)
            #print month
            if html.closed == False:
                html.close()
        return MyItems
        
    def DoubleAry(self):
        m, n = 0, 0
        NumbAry = self.RegexFilter()#call RegexFiliter function
        print (NumbAry)
        #NumSplit = [[for elem in row]for row in NumbAr]
        #NumSplit = [] * len(NumbAry)
        NumSplit =[]
        '''for index, i in enumerate(NumbAry):
            NumSplit.append([elem for elem in index])'''
        for elem in NumbAry:
            NumSplit.append([num for num in elem])
            #print(NumSplit)
    def openfile(self):
        with open("recipthtml.txt","r+") as recipttext:
            content = recipttext.read()
        recipttext.close()
        return content
recipt = GetLuck()
#recipt.SplitNumb()#call RegexFilter() It filiters the unuseful imformation
recipt.RegexFilter()
#recipt.FileSave()
#recipt.RunNumb()
#recipt.DoubleAry()
test = htmlparse.MyHTMLParser("1234")
print(test.numbers)
#test.feed(recipt.openfile())
test.generateItem
print (test.numbers)
