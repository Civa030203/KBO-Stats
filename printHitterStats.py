def printHitterStats(stats):
    print(f"{stats[1]} 소속으로 {stats[0]} 시즌에 기록한 기록입니다.\n")
    print(f'*** 시즌 타격 성적 ***\n - 시즌 타율 : {stats[2]} ({stats[5]}타수 {stats[7]}안타)\n - 총 루타 수 : {stats[11]}\n - 타점 : {stats[12]}\n - 볼넷 : {stats[15]}\n - 몸에 맞는 볼 : {stats[16]}')
    print(f' - 피삼진 : {stats[17]} (피삼진율 : {(int(stats[17]) / int(stats[5]) * 100):.3f}%)\n - 병살타 : {stats[18]}\n - 출루율 : {stats[20]}\n - 장타율 : {stats[19]}\n - OPS : {float(stats[19]) + float(stats[20]):.3f}')
    singles = int(stats[7]) - (int(stats[8]) + int(stats[9]) + int(stats[10]))
    if int(stats[7]) != 0:
        print(f'\n*** 시즌 안타 기록 ***\n - 단타 개수 : {singles} ({singles / int(stats[7]) * 100:.3f}%)')
        print(f' - 2루타 개수 : {stats[8]} ({int(stats[8]) / int(stats[7]) * 100:.3f}%)')
        print(f' - 3루타 개수 : {stats[9]} ({int(stats[9]) / int(stats[7]) * 100:.3f}%)')
        print(f' - 홈런 개수 : {stats[10]} ({int(stats[10]) / int(stats[7]) * 100:.3f}%)')
    else:
        print(f'\n*** 시즌 안타 기록 ***\n - 단타 개수 : {singles} (0.000%)')
        print(f' - 2루타 개수 : {stats[8]} (0.000%)')
        print(f' - 3루타 개수 : {stats[9]} (0.000%)')
        print(f' - 홈런 개수 : {stats[10]} (0.000%)')

    if int(stats[13]) + int(stats[14]) != 0:
        print(f'\n*** 시즌 주루 및 수비 기록 ***\n - 도루 : {stats[13]} ({stats[14]} 실패, 도루 성공율 {float(int(stats[13]) / (int(stats[13]) + int(stats[14]))) * 100:.3f}%)')
    else:
        print(f'\n*** 시즌 주루 및 수비 기록 ***\n - 도루 : 0 (0 실패, 도루 성공율 0.000%)')
    print(f' - 실책 : {stats[21]}')
