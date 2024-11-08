import math

def time_difference_in_hours(time1, time2):
    
    if not (0 <= time1 < 24) or not (0 <= time2 < 24):
        raise ValueError("Both times must be in the range [0, 24)")

    delta = time2 - time1
    if delta < 0:
        delta += 24 

    return delta

    
import unittest
class TestCyclicTime(unittest.TestCase):
def test_time_difference_in_hours(self):
        """Test calculating the correct time difference across midnight."""
        time1 = 23
        time2 = 1
        diff = time_difference_in_hours(time1, time2)
        print(f"Time difference between {time1}:00 and {time2}:00: {diff} hours")
        self.assertEqual(diff, 2, "The difference between 23:00 and 01:00 should be 2 hours")

    def test_invalid_times(self):
        """Test invalid time inputs."""
        with self.assertRaises(ValueError):
            time_to_cyclic_features(24)  

        with self.assertRaises(ValueError):
            time_difference_in_hours(25, 5)


def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCyclicTime)
    runner = unittest.TextTestRunner(verbosity=2)  
    runner.run(suite)

if __name__ == "__main__":
    run_tests()

