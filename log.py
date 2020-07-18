import datetime as dt
import os

def loggerWriter(loglst):
    month = str(dt.datetime.now().strftime('%m'))
    v = os.path.dirname(month)
    if not os.path.exists(month):
        os.mkdir(month)
    today = (str(dt.datetime.now()).split(" "))[0]
    filename = month+'/'+today+"-"+"log.txt"
    file = open(filename,'w')
    # logDic["statusCode"] = str(ret.status_code)
    # logDic["headers"] = str(ret.headers)
    # logDic["contents"]
    for logDic in loglst:
        file.write(logDic["statusCode"]+"\n"
                   +logDic["headers"]+"\n"
                   +logDic["contents"]+"\n")

    file.close()