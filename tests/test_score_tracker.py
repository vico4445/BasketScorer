import unittest
from src.score_tracker import ScoreTracker  # Assuming ScoreTracker is the class managing scores

class TestScoreTracker(unittest.TestCase):

    def setUp(self):
        """Set up a ScoreTracker instance for testing."""
        self.score_tracker = ScoreTracker()

    def test_start_game_timer(self):
        """Test if the game timer can start."""
        self.score_tracker.start_timer()
        self.assertTrue(self.score_tracker.is_timer_running)

    def test_stop_game_timer(self):
        """Test if the game timer can stop."""
        self.score_tracker.start_timer()
        self.score_tracker.stop_timer()
        self.assertFalse(self.score_tracker.is_timer_running)

    def test_reset_game_timer(self):
        """Test if the game timer can reset."""
        self.score_tracker.start_timer()
        self.score_tracker.reset_timer()
        self.assertEqual(self.score_tracker.elapsed_time, 0)

    def test_capture_points(self):
        """Test if points can be captured correctly."""
        self.score_tracker.capture_point()
        self.assertEqual(self.score_tracker.score, 1)

    def test_display_score(self):
        """Test if the score is displayed correctly."""
        self.score_tracker.capture_point()
        self.assertEqual(self.score_tracker.display_score(), "Score: 1")

if __name__ == '__main__':
    unittest.main()