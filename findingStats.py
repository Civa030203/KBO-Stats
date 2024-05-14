import time
from printHitterStats import printHitterStats
from printPitcherStats import printPitcherStats

def selectSeasonType(driver, season):
    driver.find_element_by_css_selector(f"#cphContents_cphContents_cphContents_ddlSeries > option:nth-child({season})").click()

def findingStats(driver, playerId, pos):
    if pos != "투수":
        link = str('https://www.koreabaseball.com/Record/Player/HitterDetail/Total.aspx?playerId=' + playerId)
    else:
        link = str('https://www.koreabaseball.com/Record/Player/PitcherDetail/Total.aspx?playerId=' + playerId)
    driver.get(link)
    print("데이터를 로드하는 중입니다. 잠시만 기다려주세요.")
    time.sleep(2)
    stats = []

    name = driver.find_element_by_css_selector("#cphContents_cphContents_cphContents_playerProfile_lblName").text
    team = driver.find_element_by_css_selector("#h4Team").text
    bNumber = driver.find_element_by_css_selector("#cphContents_cphContents_cphContents_playerProfile_lblBackNo").text
    year = input("기록을 검색할 연도를 입력해주세요 : ")
    season = input("기록을 검색할 시즌 종류를 선택해주세요.\n1. 정규 시즌\n2. 시범 경기\n3. 와일드카드 결정전\n4. 준플레이오프\n5. 플레이오프\n6. 한국시리즈\n선택 : ")
    selectSeasonType(driver, season)
    x = 1
    while True:
        try:
            curYear = driver.find_element_by_css_selector(f"#contents > div.sub-content > div.player_records > div > table > tbody > tr:nth-child({x}) > td:nth-child(1)").text
            if curYear == year:
                y = 1
                while True:
                    stats.append(driver.find_element_by_css_selector(f"#contents > div.sub-content > div.player_records > div > table > tbody > tr:nth-child({x}) > td:nth-child({y})").text)
                    y += 1
                break
            x += 1
        except:
            break

    seasonType = ""
    if int(season) == 1:
        seasonType = "정규시즌"
    elif int(season) == 2:
        seasonType = "시범경기"
    elif int(season) == 3:
        seasonType = "와일드카드 결정전"
    elif int(season) == 4:
        seasonType = "준플레이오프"
    elif int(season) == 5:
        seasonType = "플레이오프"
    elif int(season) == 6:
        seasonType = "한국시리즈"

    print(f'{team} No. {bNumber} {name}의 {year}년 {seasonType} 기록\n')
    if pos != "투수":
        printHitterStats(stats)
    else:
        printPitcherStats(stats)
