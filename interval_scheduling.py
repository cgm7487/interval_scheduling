from enum import Enum

class TimeType(Enum):
    TIME_TYPE_START = 0
    TIME_TYPE_END = 1

class ScheduleTime:
    def __init__(self, timeType, schTime):
        self.timeType = timeType
        self.schTime = schTime

class ScheduleData:
    def __init__(self, startTime, endTime):
        self.startTime = ScheduleTime(TimeType.TIME_TYPE_START, startTime)
        self.endTime = ScheduleTime(TimeType.TIME_TYPE_END, endTime)

test = []
test.append(ScheduleData(1, 2))
test.append(ScheduleData(2, 3))
test.append(ScheduleData(3, 4))

alltime = []
for eachTime in test:
    alltime.append(eachTime.startTime)
    alltime.append(eachTime.endTime)

alltime.sort(key=lambda schTime:schTime.schTime)

for i in range(len(alltime)-1):
    if alltime[i].timeType == alltime[i+1].timeType:
        print("Overlap!!!")
        break

