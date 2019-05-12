import unittest
import stars

class TestIsolated(unittest.TestCase):
    def test_isolated_simple(self):
        ex01 = [(0.0, 0.0),
                (1.0, 1.0),
                (23.0, 1.0),
                (2.0, 1.0)]
        indices = stars.isolated(ex01, 10.0)
        self.assertEqual(len(indices), 1)
        self.assertTrue(2 in indices)

        indices = stars.isolated(ex01, 0.0)
        self.assertEqual(len(indices), len(ex01))

        ex02 = [(0.0, 0.0),
                (1.0, 1.0),
                (2.0, 1.0),
                (0.5, 0.5),
                (1.5, 0.5)]
        indices = stars.isolated(ex02, 3.0)
        self.assertEqual(len(indices), 0)

        ex03 = [(0.0, 0.0),
                (1.0, 1.0),
                (-1.0, -1.0),
                (2.0, 1.0),
                (-2.0, 1.0),
                (-0.5, 0.5),
                (1.5, -0.5)]
        indices = stars.isolated(ex03, 10.0)
        self.assertEqual(len(indices), 0)

        ex04 = [(0.0, 0.0),
                (1.0, 1.0),
                (-1.0, -1.0),
                (2.0, 1.0),
                (-2.0, 1.0),
                (-0.5, 0.5),
                (25.0, -40.0),
                (1.5, -0.5)]
        indices = stars.isolated(ex04, 10.0)
        self.assertEqual(len(indices), 1)
        self.assertTrue(6 in indices)

    def test_isolated_nsquared(self):
        import random
        random.seed(73)
        exbig01 = [(random.random(), random.random()) for _ in range(1_000_000)]
        index_with_isolated = 434221
        exbig01[index_with_isolated] = (54.0, 12.8)
        indices = stars.isolated(exbig01, 3.0)
        self.assertEqual(len(indices), 1)
        self.assertTrue(index_with_isolated in indices)

        indices = stars.isolated(exbig01, 0.0)
        self.assertEqual(len(indices), len(exbig01))


if __name__ == "__main__":
    unittest.main()
