def ignore_exception(IgnoreException=Exception,DefaultVal=None):
    """ Decorator for ignoring exception from a function
    e.g.   @ignore_exception(DivideByZero)
    e.g.2. ignore_exception(DivideByZero)(Divide)(2/0)
    """
    def dec(function):
        def _dec(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except IgnoreException:
                return DefaultVal
        return _dec
    return dec

def numberToText(num):
    ones = " ,one,two,three,four,five,six,seven,eight,nine,ten,eleven,tweleve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty".split(',')
    tens = "ten,twenty,thirty,fourty,fifty,sixty,seventy,eighty,ninety".split(',')
    text = ""
    addAnd = True
    if len(str(num))<=2:
        if(num<20):
            text = ones[num]
        else:
            text = tens[num//10-1] +" " + ones[(num %10)]
    elif len(str(num))==3:
        text = ones[num//100] +" hundred " + ("and " if addAnd and num>100 else "") + numberToText(num- ((num//100)* 100))
    elif len(str(num))<=5:
        text = numberToText(num//1000) +" thousand " + numberToText(num- ((num//1000)* 1000))
    elif len(str(num))<=7:
        text = numberToText(num//100000) +" lakh " + numberToText(num- ((num//100000)* 100000))
    else:
        text = numberToText(num//10000000) +" crores " + numberToText(num- ((num//10000000)* 10000000))
    return text


def cleanInput(num):
    floatParser = ignore_exception(ValueError, 0.00)(float)
    intParser = ignore_exception(ValueError, 0)(int)
    num = floatParser(num)  
    strNo = "%.2f" %num
    splitDecimals = strNo.split(".")
    return intParser(splitDecimals[0]), intParser(splitDecimals[1])

def convertNumToWord(num):  
    
    wholeNumber, fractionPart = cleanInput(num)
    convertedWholeNum = numberToText(wholeNumber).strip()
    fractionpartArr = list(str(fractionPart))
    tempFractionPart = ""
    for i in fractionpartArr:
        tempFractionPart += " " + numberToText(int(i)).strip() 
    convertedFractionPart = "point" + tempFractionPart if len(tempFractionPart.strip())>0 else ""
    return (convertedWholeNum + " " + convertedFractionPart).strip().capitalize()


# print(convertNumToWord(126.44))
# print(convertNumToWord(12100))
# print(convertNumToWord(0.40))
# print(convertNumToWord(120002123.50))
# print(convertNumToWord(""))
# print(convertNumToWord(120))
# print(convertNumToWord(100))
# print(convertNumToWord(1345))
