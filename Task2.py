import numpy as np
import unittest

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

def calculate_aggregated_threat_score(department_data):
    total_weighted_score = 0
    total_weight = 0
    for data in department_data:
        mean_score = np.mean(data['scores'])
        weighted_score = mean_score * data['importance']
        total_weighted_score += weighted_score
        total_weight += data['importance']
        print(f"total_weighted_score={total_weighted_score}: total_weight = {total_weight}, calculate_aggregated_threat_score = {total_weighted_score / total_weight}")
    return total_weighted_score / total_weight if total_weight > 0 else 0

class TestAggregatedThreatScore(unittest.TestCase):

    def setUp(self):
        self.department_data_similar = [
            {'scores': generate_random_data(40, 10, 50), 'importance': 3} for _ in range(5)
        ]
        self.department_data_with_outliers = [
            {'scores': generate_random_data(20, 5, 50), 'importance': 3},
            {'scores': generate_random_data(80, 5, 50), 'importance': 3}
        ]
        self.department_data_varied_sizes = [
            {'scores': generate_random_data(30, 10, 100), 'importance': 4},
            {'scores': generate_random_data(50, 15, 20), 'importance': 5},
            {'scores': generate_random_data(25, 10, 150), 'importance': 2}
        ]

    def test_similar_departments(self):
        result = calculate_aggregated_threat_score(self.department_data_similar)
        self.assertTrue(0 <= result <= 90, "Score should be within 0-90 range")

    def test_with_outliers(self):
        result = calculate_aggregated_threat_score(self.department_data_with_outliers)
        self.assertTrue(0 <= result <= 90, "Score should be within 0-90 range")

    def test_varied_department_sizes(self):
        result = calculate_aggregated_threat_score(self.department_data_varied_sizes)
        self.assertTrue(0 <= result <= 90, "Score should be within 0-90 range")

    def test_calculate_aggregated_threat_score_zero_weight(self):
        department_data = [{'scores': generate_random_data(40, 10, 50), 'importance': 0}]
        result = calculate_aggregated_threat_score(department_data)
        self.assertEqual(result, 0, "If all departments have zero importance, result should be 0")

    def test_generate_random_data_range(self):
        data = generate_random_data(50, 20, 100)
        self.assertTrue(all(0 <= x <= 90 for x in data), "Generated data should be within 0-90 range")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAggregatedThreatScore)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
