# 項目37 組み込み型の深い入れ子にはせずクラスを作成する
from collections import defaultdict
from collections import namedtuple


class SimpleGradebook:
    """
    最もシンプルな成績管理
    """
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []
    
    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


class BySubjectGradebook:
    """
    生徒、科目毎の点数を管理する
    """
    def __init__(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = defaultdict(list)
    
    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        print(by_subject.values())
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


class WeightedGradebook:
    """
    科目ごとの点数に重み付けをして管理する
    """
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        """[summary]

        Args:
            name ([str]): student name
            subject ([str]): subject name
            score ([float]): score
            weight ([float]): weight by subject
        """
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))
    
    def average_grade(self, name):
        """average_grade

        Args:
            name ([str]): [name of person]

        Returns:
            double: average of score
        """
        by_subject = self._grades[name]

        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            
            score_sum += subject_avg / total_weight
            score_count += 1
        
        return score_sum / score_count


Grade = namedtuple('Grade', ('score', 'weight'))


class Subject:
    """
    一群の成績を含む一つの科目を表すクラス
    """
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    """
    ある1人に学生が選択している科目
    """
    def __init__(self):
        self._subjects = defaultdict(Subject)
    
    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    """
    名前をキーにして動的に処理できるすべての学生のコンテナ
    """
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


if __name__ == '__main__':
    # book = SimpleGradebook()
    # book = BySubjectGradebook()
    # book = WeightedGradebook()
    # book.add_student('Isaac Newton')
    # book.report_grade('Isaac Newton', 'Math', 75, 0.05)
    # book.report_grade('Isaac Newton', 'Math', 65, 0.15)
    # book.report_grade('Isaac Newton', 'Gym', 90, 0.8)
    # book.report_grade('Isaac Newton', 'Gym', 95, 0.6)
    # val = book.average_grade('Isaac Newton')
    # print(type(val))
    # print(book.average_grade('Isaac Newton'))

    # grades = []
    # print(type(grades))
    # grades.append((95, 0.45))
    # grades.append((85, 0.55))
    # total = sum(score * weight for score, weight in grades)
    # total_weight = sum(weight for _, weight in grades)
    # average_grade = total / total_weight
    # print(average_grade)
    # print((((95 * 0.45) + (85 * 0.55))) / 1)

    book = Gradebook()
    albert = book.get_student('Albert Einstein')
    math = albert.get_subject('Math')
    math.report_grade(75, 0.05)
    math.report_grade(65, 0.15)
    math.report_grade(70, 0.80)
    gym = albert.get_subject('Gym')
    gym.report_grade(100, 0.4)
    gym.report_grade(85, 0.6)
    print(albert.average_grade())
    print(gym.average_grade())
    print(math.average_grade())
