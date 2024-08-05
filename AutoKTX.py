def getUserInput():
    departure = input("출발역을 입력하세요: ")
    arrival = input("도착역을 입력하세요: ")
    date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    time = input("시간을 입력하세요 (HH:MM): ")
    return departure, arrival, date, time

import pandas as pd

def loadSchedule():
    data = {
        "출발역": ["서울", "서울", "대전", "대전"],
        "도착역": ["대전", "부산", "부산", "서울"],
        "날짜": ["2024-08-05", "2024-08-05", "2024-08-05", "2024-08-05"],
        "시간": ["09:00", "10:00", "11:00", "12:00"],
        "열차번호": [101, 102, 103, 104]
    }
    df = pd.DataFrame(data)
    return df

def searchSchedule(df, departure, arrival, date, time):
    results = df[(df["출발역"] == departure) &
                 (df["도착역"] == arrival) &
                 (df["날짜"] == date) &
                 (df["시간"] >= time)]
    return results

def bookTrain(schedule):
    if schedule.empty:
        print("해당 조건에 맞는 열차가 없습니다.")
        return None

    print("예약 가능한 열차:")
    print(schedule)
    
    trainNumber = input("예약할 열차번호를 입력하세요: ")
    if int(trainNumber) in schedule["열차번호"].values:
        print(f"열차 {trainNumber}번이 예약되었습니다.")
        return int(trainNumber)
    else:
        print("잘못된 열차번호입니다.")
        return None

def main():
    departure, arrival, date, time = getUserInput()
    schedule = loadSchedule()
    results = searchSchedule(schedule, departure, arrival, date, time)
    bookedTrain = bookTrain(results)
    
    if bookedTrain:
        print(f"열차 {bookedTrain}번 예약 완료!")
    else:
        print("예약에 실패했습니다.")

if __name__ == "__main__":
    main()