from importlib.util import find_spec
from pathlib import Path


SUPPORTED_MODULES = {
    "image": ("image_module", "extract_text_from_image", "Image"),
    "text": ("utils.text_module", "process_text", "Text"),
    "audio": ("utils.audio_module", "extract_text_from_audio", "Audio"),
}


def module_available(module_name):
    """Return whether an optional modality module is available."""
    return find_spec(module_name) is not None


def run_modality(file_type, file_path):
    """Load the selected modality lazily and return its processing result."""
    if file_type not in SUPPORTED_MODULES:
        raise ValueError("Unsupported type. Choose image, text, or audio.")

    path = Path(file_path).expanduser()
    if not file_path or not path.is_file():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    module_name, function_name, _ = SUPPORTED_MODULES[file_type]
    if not module_available(module_name):
        raise ModuleNotFoundError(
            f"The {file_type} processing module is not available in this checkout."
        )

    module = __import__(module_name, fromlist=[function_name])
    processor = getattr(module, function_name)
    return processor(str(path))


def main():
    print("Select a file (Image, Text, or Audio):")
    file_type = input().strip().lower()

    if file_type not in SUPPORTED_MODULES:
        print("Unsupported type. Please choose image, text, or audio.")
        return

    display_name = SUPPORTED_MODULES[file_type][2]
    print(f"Enter the path to the {display_name.lower()} file:")
    file_path = input().strip()

    try:
        result = run_modality(file_type, file_path)
        print(f"{display_name} result:", result)
    except (FileNotFoundError, ModuleNotFoundError, ValueError) as exc:
        print("Unable to process the selected file:", exc)


if __name__ == "__main__":
    main()
