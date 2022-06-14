medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point

def createMedalTable(results):
    resultsTable = {}
    count = 0
    for sport in medalResults:

        podium = sport["podium"]

        for country in podium:
            medalToPoints = { '1' : 3, '2' : 2, '3' : 1}
 
            position = country[0:1]
            print(position, "position")
            
            if (resultsTable.get(country[2:]) == None):
                count += 1
                print(count, "count")
                resultsTable[country[2:]] = medalToPoints[country[0:1]]
            else:
                print(medalToPoints[country[0:1]], "medal to points in else")
                resultsTable[country[2:]] += medalToPoints[country[0:1]]

            #add score to country
            
          #  print(medalToPoints[1], "medalToPoints")
            print(resultsTable["China"], "check")
            print(resultsTable, "resultsTable")
            print("----------------------------")

    print(resultsTable)
    return resultsTable


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
