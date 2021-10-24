import math 


def get_average(numbers):
  return sum(numbers)/len(numbers)


class EmailAlert():
  def __init__(self):
    self.emailSent = False


class LEDAlert():
  def __init__(self):
    self.ledGlows = False


class StatsAlerter():
  def __init__(self, maxThreshold, alert):
    self.maxThreshold = maxThreshold
    self.emailAlert = alert[0]
    self.ledAlert = alert[1]

  def checkAndAlert(self, numberList):
    for number in numberList:
      if number > self.maxThreshold:
        self.emailAlert.emailSent = True
        self.ledAlert.ledGlows = True


def calculateStats(numbers):
  computedStats = {}
  if len(numbers) == 0:
    computedStats["avg"] = math.nan
    computedStats["max"] = math.nan
    computedStats["min"] = math.nan
    return computedStats
  
  computedStats["avg"] = get_average(numbers)
  computedStats["max"] = max(numbers)
  computedStats["min"] = min(numbers)
   
  return computedStats
