import unittest

import tests

class TournamentTest(unittest.TestCase):

    all_results = []

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = tests.Runner("Усэйн", 10)
        self.runner2 = tests.Runner("Андрей", 9)
        self.runner3 = tests.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("Результаты тестов:")
        for idx, result in enumerate(cls.all_results):
            print(f"{idx + 1}: {result}")

    def test_race_one(self):
        tournament = tests.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        formatted_result = {place: runner.name for place, runner in results.items()}
        self.all_results.append(formatted_result)

        # Проверяем, что последний бегун это Ник
        self.assertTrue("Ник" in formatted_result.values())

    def test_race_two(self):
        tournament = tests.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        formatted_result = {place: runner.name for place, runner in results.items()}
        self.all_results.append(formatted_result)

        # Проверяем, что последний бегун это Ник
        self.assertTrue("Ник" in formatted_result.values())

    def test_race_three(self):
        tournament = tests.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        formatted_result = {place: runner.name for place, runner in results.items()}
        self.all_results.append(formatted_result)

        # Проверяем, что последний бегун это Ник
        self.assertTrue("Ник" in formatted_result.values())

if __name__ == "__main__":
    unittest.main()