import lecture4_home_task as lec4_ht
import pytest


@pytest.mark.parametrize(
    "data_test",
    [([{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {
        'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}])]
)
def test_task_1(data_test):
    result_test = lec4_ht.task_1()
    assert data_test == result_test


@pytest.mark.parametrize(
    "data_test",
    [([98, 35, 213, 54, 119, 15])]
)
def test_task_2(data_test):
    result_test = lec4_ht.task_2()
    assert data_test == result_test


@pytest.mark.parametrize(
    "data_test",
    [({1: 12.5, 3: 50.0, 2: 37.5})]
)
def test_task_3(data_test):
    result_test = lec4_ht.task_3()
    assert data_test == result_test


@pytest.mark.parametrize(
    "data_test",
    [([120, 'yandex'])]
)
def test_task_4(data_test):
    result_test = lec4_ht.task_4()
    assert data_test == result_test
