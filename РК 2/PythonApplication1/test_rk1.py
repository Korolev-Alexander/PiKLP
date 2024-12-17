import unittest
from rk1_refactored import Student, Department, link_students_to_departments, query_1, query_2, query_3

class TestRK1(unittest.TestCase):

    def setUp(self):
        self.students = [
            Student(1, "Королев", 10000, 1),
            Student(2, "Петров", 12000, 1),
            Student(3, "Пронин", 11000, 2),
            Student(4, "Иванов", 13000, 2),
            Student(5, "Смирнов", 14000, 3)
        ]

        self.departments = [
            Department(1, "Кафедра математики"),
            Department(2, "Кафедра физики"),
            Department(3, "Кафедра информатики")
        ]

        link_students_to_departments(self.students, self.departments)
    #Проверяет, что функция query_1 возвращает правильное количество кафедр и студентов.
    def test_query_1(self):
        result = query_1(self.departments)
        self.assertEqual(len(result), 3)
        self.assertEqual(len(result[0][1]), 2)
        self.assertEqual(len(result[1][1]), 2)
        self.assertEqual(len(result[2][1]), 1)
    #Проверяет, что функция query_2 возвращает правильные суммы стипендий для каждой кафедры.
    def test_query_2(self):
        result = query_2(self.departments)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][1], 24000)
        self.assertEqual(result[1][1], 22000)
        self.assertEqual(result[2][1], 14000)
    #Проверяет, что функция query_3 возвращает только те кафедры, в названии которых есть слово "кафедра".
    def test_query_3(self):
        result = query_3(self.departments)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][0].name, "Кафедра математики")
        self.assertEqual(result[1][0].name, "Кафедра физики")
        self.assertEqual(result[2][0].name, "Кафедра информатики")

if __name__ == "__main__":
    unittest.main()