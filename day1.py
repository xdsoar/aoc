def getInputArray():
    f = open('day1.txt')
    inputText = f.read()
    intputLine = inputText.split('\n')
    f.close()
    return intputLine

def partOne():
    intputLine = getInputArray()
    previousNumber = None
    increseNumber = 0
    for number in intputLine:
        if previousNumber is not None  and previousNumber < int(number):
            increseNumber = increseNumber + 1
        previousNumber = int(number)
    print(increseNumber)

def popAndInsert(arr, newMember):
    newArr = arr[1:].append(newMember)

def partTwo():
    intputLine = getInputArray()
    increseNumber = 0
    previousNumbers = []
    currNumbers = []
    for number in intputLine:
        if len(currNumbers) >= 3:
            currNumbers = currNumbers[1:]
        currNumbers.append(int(number))
        print('numer is ' + number + ' and curr is ' + str(currNumbers) + ' and pre is' + str(previousNumbers))
        if len(previousNumbers) == 3 and sum(currNumbers) > sum(previousNumbers):
            increseNumber = increseNumber + 1
            print('increse!')
        previousNumbers = currNumbers
    print(increseNumber)


if __name__ == "__main__":
    partOne()
    partTwo()