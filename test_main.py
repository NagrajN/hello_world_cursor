import unittest
from io import StringIO
from unittest.mock import patch

from main import add, main


class TestMain(unittest.TestCase):

    def test_output_matches_specification(self):
        """main() must print exactly 'I am the world' per plan.md."""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            self.assertEqual(mock_stdout.getvalue(), "I am the world\n")

    def test_output_is_single_line(self):
        """main() must produce exactly one line of output."""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            lines = mock_stdout.getvalue().splitlines()
            self.assertEqual(len(lines), 1)

    def test_output_contains_no_trailing_whitespace(self):
        """The printed line must not have leading or trailing whitespace."""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            line = mock_stdout.getvalue().rstrip("\n")
            self.assertEqual(line, line.strip())

    def test_main_returns_none(self):
        """main() must return None (no explicit return value)."""
        with patch("sys.stdout", new_callable=StringIO):
            result = main()
        self.assertIsNone(result)


class TestAdd(unittest.TestCase):

    def test_add_two_positive_integers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_positive_and_negative(self):
        self.assertEqual(add(10, -4), 6)

    def test_add_two_negative_integers(self):
        self.assertEqual(add(-3, -7), -10)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=10)

    def test_add_zero_identity(self):
        self.assertEqual(add(0, 42), 42)
        self.assertEqual(add(42, 0), 42)

    def test_add_returns_correct_type_for_ints(self):
        self.assertIsInstance(add(1, 2), int)

    def test_add_returns_correct_type_for_floats(self):
        self.assertIsInstance(add(1.0, 2.0), float)


if __name__ == "__main__":
    unittest.main()
