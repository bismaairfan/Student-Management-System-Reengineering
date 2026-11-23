
import unittest
from importlib.util import spec_from_file_location, module_from_spec

spec = spec_from_file_location(
    "student_management",
    "Student-Management-System.py"
)
module = module_from_spec(spec)
spec.loader.exec_module(module)

StudentDatabase = module.StudentDatabase


class TestStudentDatabase(unittest.TestCase):

    def setUp(self):
        self.db = StudentDatabase(":memory:")

    def tearDown(self):
        self.db.close()

    def test_new_record_does_not_exist(self):
        result = self.db.record_exists(
            "Ali", "03001234567", "ali@gmail.com", "BSSE-01", "SE"
        )
        self.assertFalse(result)

    def test_inserted_record_exists(self):
        self.db.insert(
            "Ali", "03001234567", "ali@gmail.com", "BSSE-01", "SE"
        )
        result = self.db.record_exists(
            "Ali", "03001234567", "ali@gmail.com", "BSSE-01", "SE"
        )
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
