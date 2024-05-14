from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from findingStats import findingStats
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options = options)

def findStats(driver, playerId, position):
    findingStats(driver, playerId, position)

#크롬 드라이버에 url 주소 넣고 실행
def findPlayer():
    playerName = input('검색할 선수의 이름을 입력해주세요 : ')
    link = str('https://www.koreabaseball.com/Player/Search.aspx?searchWord=' + playerName)
    driver.get(link)
    print("검색 중입니다. 잠시만 기다려주세요.")
    time.sleep(2)
    resultCounts = driver.find_element_by_css_selector("#cphContents_cphContents_cphContents_udpRecord > div.inquiry > p > strong > span")
    resultCounts = int(resultCounts.text)

    if resultCounts == 0:
        print("검색된 선수가 없습니다.")
        return 0

    playerNumbers = []
    playerNames = []
    playerTeams = []
    playerPoss = []
    playerIds = []

    for x in range(1, resultCounts + 1):
        playerNumber = driver.find_element_by_css_selector("#cphContents_cphContents_cphContents_udpRecord > div.inquiry > table > tbody > tr:nth-child(" + str(x) + ") > td:nth-child(1)")
        playerName = driver.find_element_by_css_selector("#cphContents_cphContents_cphContents_udpRecord > div.inquiry > table > tbody > tr:nth-child(" + str(x) + ") > td:nth-child(2) > a")
        playerTeam = driver.find_element_by_css_selector("#cphContents_cphContents_cphContents_udpRecord > div.inquiry > table > tbody > tr:nth-child(" + str(x) + ") > td:nth-child(3)")
        playerPos = driver.find_element_by_css_selector("#cphContents_cphContents_cphContents_udpRecord > div.inquiry > table > tbody > tr:nth-child(" + str(x) + ") > td:nth-child(4)")
        playerId = playerName.get_attribute("href")
        playerId = playerId[-5:]
        playerNumbers.append(playerNumber.text)
        playerNames.append(playerName.text)
        playerTeams.append(playerTeam.text)
        playerPoss.append(playerPos.text)
        playerIds.append(playerId)
    while True:
        for x in range(len(playerNames)):
            print(f'{x + 1}. {playerTeams[x]} No. {playerNumbers[x]} {playerPoss[x]} {playerNames[x]} (ID : {playerIds[x]})')
        selectedPlayer = input('찾을 선수의 ID를 입력해주세요 : ')
        if selectedPlayer not in playerIds:
            print("잘못된 입력입니다! 다시 입력해주세요. ")
        else:
            index = 0
            for x in range(len(playerIds)):
                if playerIds[index] == selectedPlayer:
                    position = playerPoss[index]
                else:
                    index += 1
            findStats(driver, str(selectedPlayer), position)
            break

if __name__ == '__main__':
    findPlayer()
    driver.quit()
