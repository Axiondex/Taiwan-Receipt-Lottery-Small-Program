from html.parser import HTMLParser
from html.entities import name2codepoint
class MyHTMLParser(HTMLParser):
    numbers = []
    def __init__(self,htmltext):
        HTMLParser.__init__(self)
        self.isNumber = False
        self.__numbers = []
        self.__titles =[]
        self.isTitle = False
        self.isRewardName = False
        self.htmltext = htmltext
    def handle_starttag(self,tag,attrs):
        if tag == 'span' and attrs == [('class', 't18Red')]:
            self.isNumber = True
        if tag == 'h2' and attrs == []:
            self.isTitle = True
        if tag == 'td' and attrs ==[('class','title')]:
            self.isRewardName = True;

        #print(attrs)
        sattrs = set(attrs)
        #print (s)
        classattr = ('class', 't18Red')
        if classattr in sattrs:
            self.isNumber = True
            #print(tag, attrs)
    def handle_data(self,data):
        if self.isNumber:
            self.numbers.append(data.split('、'))
            #self.numbers.append(data)
            self.isNumber = False
            #print(self.numbers)
            #print (data)
        if self.isTitle:
            self.isTitle = False
            self.titles.append(data)
            #print (data)
        if self.isRewardName:
            self.isRewardName = False
            #print (data)
        #print (data)
        #print (self.numbers)
    def generateItem(self):
        self.feed(self.htmltext)
    @property
    def numbers(self):
        return self.__numbers
    @property
    def titles(self):
        return self.__titles
