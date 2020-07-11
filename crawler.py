#-*- encoding: euc-kr -*-

import requests
import json
from bs4 import BeautifulSoup
import enums
import yaml
import log

class Crawler:
    def __init__(self,url):
        self.url = url
        self.html = requests.get(url)
        self.html.encoding = 'ANSI'
        self.soup = BeautifulSoup(self.html.text,enums.PARSER)
        self.dataLst = []
        self.loglst = []
        self.apiUrl = ""
        with open('resource/info.yaml') as f:
            self.info =yaml.load(f)

    def genPlayDic(self,nameStr,goalsScore,assistsInfo,teamInfo,minutesPerGoalInfo,minutesPlayedInfo,totalShotsInfo,shotsOnTargetInfo):
        player = {}
        player["playerName"] = self.soup.select(nameStr)[0].contents[0]
        player["goalScore"] = self.soup.select(goalsScore)[0].contents[0]
        player["assists"] = self.soup.select(assistsInfo)[0].contents[0]
        player["teamName"] = self.soup.select(teamInfo)[0].contents[0]
        player["minutesperGoal"] = self.soup.select(minutesPerGoalInfo)[0].contents[0]
        player["minutesPlayed"] = self.soup.select(minutesPlayedInfo)[0].contents[0]
        player["totalShots"] = self.soup.select(totalShotsInfo)[0].contents[0]
        player["shotsOnTarget"] = self.soup.select(shotsOnTargetInfo)[0].contents[0]
        player["season"] = self.info["season"]

        return player

    def doCrawling(self):
        index = 1
        while True:
            try:
                selectNameStr = "#top-scorers > ol > li:nth-child({0}) > div > div.top-player-stats__body > h2".format(index)
                selectGoalsScore = "#top-scorers > ol > li:nth-child({0}) > div > div.top-player-stats__body > div > div.top-player-stats__main-stats " \
                                  "> p.top-player-stats__goals-scored > span.top-player-stats__goals-scored-number".format(index)
                selectAssists = "#top-scorers > ol > li:nth-child({0}) > div > div.top-player-stats__body > div > " \
                                "div.top-player-stats__main-stats > p.top-player-stats__assists > span.top-player-stats__assists-number.gel-double-pica".format(index)
                selectTeamInfo = "#top-scorers > ol > li:nth-child({0}) > div > div.top-player-stats__body > div > div.top-player-stats__details > div > span".format(index)
                selectMinutesPerGoal = "#top-scorers > ol > li:nth-child({0}) > div > div.top-player-stats__body > div > " \
                                       "div.top-player-stats__details > p.top-player-stats__mins-per-goal.gel-long-primer".format(index)
                selectMinutesPlayed = "#top-scorers > ol > li:nth-child({0}) > div > div.top-player-stats__body > div " \
                                      "> div.top-player-stats__details > p.top-player-stats__mins-played.gel-long-primer".format(index)
                selectTotalShots = "#top-scorers > ol > li:nth-child({0}) > div > div.top-player-stats__body > div > " \
                                   "div.top-player-stats__chart > div > div > span.percentage-bar-chart__total.gel-pica.shots-total".format(index)
                selectShotsOnTarget = "#top-scorers > ol > li:nth-child({0}) > div > div.top-player-stats__body > div > " \
                                      "div.top-player-stats__chart > div > div > div > span > span > span".format(index)
                p = self.genPlayDic(selectNameStr,selectGoalsScore,selectAssists,selectTeamInfo,selectMinutesPerGoal,selectMinutesPlayed,selectTotalShots,selectShotsOnTarget)
                # print(p.__str__())
                self.dataLst.append(p)
                index+=1
            except IndexError as e:
                print("=================== ErrorLine ================")
                print("indexError and index: "+str(index))
                break

    def toJson(self,obj):
        return json.dumps(obj)

    def reqAPI(self,apiUrl):
        self.apiUrl = apiUrl
        headers = {'Content-type': 'application/json', 'accept': 'application/json'}
        for playinfo in self.dataLst:
            data = playinfo
            ret = requests.post(apiUrl,data=json.dumps(data),headers=headers)
            logDic = {}
            logDic["statusCode"]=str(ret.status_code)
            logDic["headers"]=str(ret.headers)
            logDic["contents"]=ret.text
            self.loglst.append(logDic)
        log.loggerWriter(self.loglst)