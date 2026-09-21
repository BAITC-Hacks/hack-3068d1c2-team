import unittest
from pathlib import Path
from check import classify

class ClassifierTests(unittest.TestCase):
    def test_demo_images(self):
        self.assertEqual(classify(Path("ok.png"))[0], "OK")
        self.assertEqual(classify(Path("defect.png"))[0], "DEFECT")

if __name__ == "__main__":
    unittest.main()
