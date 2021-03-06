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

    for dictionary in medalResults:
        podium = dictionary["podium"]

        for currentCountry in podium:
            medalToPoints = { '1' : 3, '2' : 2, '3' : 1}
            country = currentCountry[2:]
            countryPosition = currentCountry[0:1]
            
            if (resultsTable.get(country) == None):
                resultsTable[country] = medalToPoints[countryPosition]
            else:
                resultsTable[country] += medalToPoints[countryPosition]

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
