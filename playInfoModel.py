class PlayInfo:
    def __init__(self,playName,goalsScore,assists,teamName,minutesPerGoal,minutesPlayed,totalShots,shotsOnTarget):
        self.__playName = playName
        self.__GoalsScore = goalsScore
        self.__Assists = assists
        self.__TeamName = teamName
        self.__MinutesPerGoal = minutesPerGoal
        self.__MinutesPlayed = minutesPlayed
        self.__TotalShots = totalShots
        self.__ShotsOnTarget = shotsOnTarget

    @property
    def playName(self):
        return self.__playName

    @property
    def GoalsScore(self):
        return self.__GoalsScore

    @property
    def Assists(self):
        return self.__Assists

    @property
    def TeamName(self):
        return self.__TeamName

    @property
    def MinutesPerGoal(self):
        return self.__MinutesPerGoal

    @property
    def MinutesPlayed(self):
        return self.__MinutesPlayed

    @property
    def TotalShots(self):
        return self.__TotalShots

    @property
    def ShotsOnTarget(self):
        return self.__ShotsOnTarget

    def __str__(self) -> str:
        return self.__playName+" "+self.__GoalsScore+" "+self.__Assists+" "+self.__TeamName+" "+self.__MinutesPerGoal+" " \
            +self.__MinutesPlayed+" "+self.__TotalShots+" "+self.__ShotsOnTarget

