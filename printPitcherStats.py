def printPitcherStats(stats):
    print(f'{stats[1]} 소속으로 {stats[0]} 시즌에 기록한 기록입니다.\n')
    print(f'*** 시즌 투구 기록 ***\n - 등판 : {stats[3]}경기 ({stats[4]}완투)\n - 평균자책점 : {stats[2]}\n - 투구 이닝 : {stats[12]}\n - 실점 : {stats[18]} ({stats[19]} 자책)\n - 승 : {stats[6]} (승률 : {float(stats[10]) * 100}%)\n - 패 : {stats[7]}\n - 세이브 : {stats[8]}\n - 홀드 : {stats[9]}')
    print(f'\n*** 시즌 피안타 기록 ***\n - 상대 타자 수 : {stats[11]}\n - 피안타 : {stats[13]}\n - 피홈런 : {stats[14]}\n - 허용 4사구 : {int(stats[15]) + int(stats[16])}\n - 탈삼진 : {stats[17]} (탈삼진율 : {(int(stats[17]) / int(stats[11])) * 100}%)')
    print(stats)
