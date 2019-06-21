def numberToText(no):
    ones = " ,one,two,three,four,five,six,seven,eight,nine,ten,eleven,tweleve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty".split(',')
    tens = "ten,twenty,thirty,fourty,fifty,sixty,seventy,eighty,ninety".split(',')
    text = ""
    if len(str(no))<=2:
        if(no<20):
            text = ones[no]
        else:
            text = tens[no//10-1] +" " + ones[(no %10)]
    elif len(str(no))==3:
        text = ones[no//100] +" hundred " + numberToText(no- ((no//100)* 100))
    elif len(str(no))<=5:
        text = numberToText(no//1000) +" thousand " + numberToText(no- ((no//1000)* 1000))
    elif len(str(no))<=7:
        text = numberToText(no//100000) +" lakh " + numberToText(no- ((no//100000)* 100000))
    else:
        text = numberToText(no//10000000) +" crores " + numberToText(no- ((no//10000000)* 10000000))
    return text
    
def convertNumToWord(no):    
    strNo = "%.2f" %no
    n = strNo.split(".")
    rs = numberToText(int(n[0])).strip()
    ps =""
    if(len(n)>=2):
        ps = numberToText(int(n[1])).strip()
        rs = "" + ps+ " paise"  if(rs.strip()=="") else  (rs + " and " + ps+ " paise").strip()
    return rs
