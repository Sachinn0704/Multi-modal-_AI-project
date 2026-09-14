import unittest
from unittest.mock import patch

import app


class AppTests(unittest.TestCase):
    def test_run_modality_rejects_unknown_type(self):
        with self.assertRaisesRegex(ValueError, "Unsupported type"):
            app.run_modality("video", "sample.mp4")

    @patch("app.module_available", return_value=False)
    def test_run_modality_reports_missing_optional_module(self, _available):
        with self.assertRaisesRegex(ModuleNotFoundError, "image processing module"):
            app.run_modality("image", "sample.png")

    @patch("app.module_available", return_value=True)
    @patch("app.__import__")
    def test_run_modality_loads_processor_lazily(self, mock_import, _available):
        processor = mock_import.return_value.extract_text_from_image
        processor.return_value = "detected text"

        result = app.run_modality("image", "sample.png")

        self.assertEqual(result, "detected text")
        mock_import.assert_called_once_with("image_module", fromlist=["extract_text_from_image"])
        processor.assert_called_once_with("sample.png")


if __name__ == "__main__":
    unittest.main()
