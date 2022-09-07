while True:
    string_input = input("정수 입력>")
    if string_input.isdigit():
        number_input_a = int(string_input)
        print("원의 반지름:"), number_input_a)
        print("원의 둘레:", 2 * 3.14 * number_input_a)
        print("원의 넓이:, 3.14 * number_input_a * number_input_a")
        break
    else:
        print("정수 입력해라 김가인")



list_input_a = ["15","365","김가인바보멍청이똥개","948735973498597589375"]

List_number = []
for item in list_input_a:
    try:
        float(itme)
        list_number.append(item)
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))



try:
    number = int(input(">정수 입력"))
    print("입력 값은 {}입니다.".format(number))
except:
    print("예외 발생 ㅅㄱ")
finally:
    print("무조건 실행 ㅅㄱ")


class 학생:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def 총점(self):
    return self.korean + self.math +\
        self.english + self.science
    def 출력(self):
        print(self.name, self.총점(), self.평균(), sep="\t")

student = [
    학생("김가인", 13, 24, 53, 28),
    학생("박시후", 0, 0, 0, 0),
    학생("김민준", 10, 100, 10, 10)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    student.출력()


class Student:
    def __init__(self, 이름, 나이):
        print("객체가 생성됨ㅇㅇ")
        self.이름 = 이름
        self.나이 = 나이
    def __del__(self):
        print("객체가 소멸됨ㅇㅇ")
    def 출력(self):
        print(self.이름, self.나이)

student = Student("윤인성", 3)
student.출력()