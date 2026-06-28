import unittest
from reposentinel.cli import explain, has_blocked_path

class RepoSentinelTest(unittest.TestCase):
    def test_explain(self):
        self.assertEqual(explain(), 0)

    def test_blocked_path(self):
        self.assertTrue(has_blocked_path("x/node_modules/react/index.js"))
        self.assertTrue(has_blocked_path(".env"))
        self.assertFalse(has_blocked_path("src/app.py"))

if __name__ == "__main__":
    unittest.main()
