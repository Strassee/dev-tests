from unittest import TestCase, expectedFailure, skipIf
import pytest

from main import unique_names, top3_names, duration_courses, MENTORS, COURSES, DURATIONS



class TestUnittest(TestCase):

    def test_unique_names(self):
        expected_names = ['Адилет', 'Азамат', 'Александр', 'Алексей', 'Алена', 'Анатолий', 'Анна', 'Антон', 'Вадим', 'Валерий', 'Владимир', 'Денис', 'Дмитрий', \
        'Евгений', 'Елена', 'Иван', 'Илья', 'Кирилл', 'Константин', 'Максим', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Ринат', 'Роман', \
        'Сергей', 'Татьяна', 'Тимур', 'Филипп', 'Эдгар', 'Юрий']
        names = unique_names(MENTORS)
        self.assertListEqual(names, expected_names)
    
    def test_top3_names(self):
        names = top3_names(MENTORS)
        expected_names = ['Александр', 'Евгений', 'Максим']
        self.assertListEqual(names, expected_names)
    
    def test_duration_courses(self):
        duration_course = duration_courses(COURSES, DURATIONS)
        expected_duration_course = {12: [2], 14: [0], 20: [1, 3]}
        self.assertDictEqual(duration_course, expected_duration_course)

class TestPytestNames():

    @pytest.mark.parametrize(
        "mentors, expected, expected_top_3", [
            (MENTORS, ['Адилет', 'Азамат', 'Александр', 'Алексей', 'Алена', 'Анатолий', 'Анна', 'Антон', 'Вадим', 'Валерий', 'Владимир', 'Денис', 'Дмитрий', \
                       'Евгений', 'Елена', 'Иван', 'Илья', 'Кирилл', 'Константин', 'Максим', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Ринат', 'Роман', \
                        'Сергей', 'Татьяна', 'Тимур', 'Филипп', 'Эдгар', 'Юрий'], ['Александр', 'Евгений', 'Максим']),
            ([["Евгений Шек", "Иван Маркитан", "Алена Батицкая", "Александр Фитискин"],["Евгений Шмаргунов", "Иван Бочаров", "Александр Иванов"]], ["Александр", "Алена", "Евгений", "Иван"], ["Александр", "Евгений", "Иван"]),
        ]
    )

    def test_names(self, mentors, expected, expected_top_3):
        names = unique_names(mentors)
        top_names = top3_names(mentors)
        print(top_names)
        print(expected_top_3)
        assert names == expected
        assert top_names == expected_top_3


class TestPytestCourses():

    @pytest.mark.parametrize(
        "courses, duration, expected", [
            (COURSES, DURATIONS, {12: [2], 14: [0], 20: [1, 3]}),
            (COURSES, [7, 9, 3, 2], {2: [3], 3: [2], 7: [0], 9: [1]}),
        ]
    )

    def test_duration_courses(self, courses, duration, expected):
        duration_course = duration_courses(courses, duration)
        assert duration_course == expected