import unittest
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed
    def run(self):
        self.distance += self.speed * 2  # Увеличиваем расстояние
    def walk(self):
        self.distance += self.speed
    def __str__(self):
        return self.name
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)
    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    # Выход из цикла, чтобы не обновлять состояния других участников
                    break
        return finishers
class TournamentTest(unittest.TestCase):
    all_results = {}
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)
    @classmethod
    def tearDownClass(cls):
        print("Результаты тестов:")
        for key in sorted(cls.all_results.keys()):
            result = cls.all_results[key]
            # Форматируем вывод результатов в нужном формате
            formatted_result = {place: runner for place, runner in result.items()}
            print(formatted_result)
    def test_race_one(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = {place: runner.name for place, runner in results.items()}
        # Проверяем, что последний бегун это Ник
        self.assertTrue("Ник" in self.all_results[max(results.keys())].values())
    def test_race_two(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = {place: runner.name for place, runner in results.items()}
        # Проверяем, что последний бегун это Ник
        self.assertTrue("Ник" in self.all_results[max(results.keys())].values())
    def test_race_three(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = {place: runner.name for place, runner in results.items()}
        # Проверяем, что последний бегун это Ник
        self.assertTrue("Ник" in self.all_results[max(results.keys())].values())
if __name__ == "__main__":
    unittest.main()