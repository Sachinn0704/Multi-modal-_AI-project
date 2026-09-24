# Multimodal AI Interaction System

A Python-based multimodal AI project that brings together text, image, and speech processing concepts in a single application workflow.

## Project Summary

The project demonstrates how different input modalities can be routed to appropriate processing components and exposed through one application. The repository currently contains a main application entry point and a dedicated image-processing module.

## Main Features

- Text input processing
- Image loading and inference workflow
- Speech/audio interaction workflow
- AI model orchestration across modalities
- Application-level interface through the main Python entry point

## Technology Stack

- Python
- NLP / transformer-based processing concepts
- CNN / computer-vision processing concepts
- Audio/speech processing
- NumPy and other project dependencies listed in `requirements.txt`

## Project Structure

```text
.
├── LICENSE
├── README.md
├── app.py
├── image_module.py
├── requirements.txt
└── tests/
    └── test_app.py
```

## How It Works

1. The application asks which modality should be processed: `image`, `text`, or `audio`.
2. The selected input file path is validated before the modality processor is loaded.
3. The input is routed to the relevant processing component.
4. The corresponding AI/model-processing component generates an output.
5. The application prints the resulting response or a clear processing error.

The dispatcher loads modality modules lazily, so a missing optional processor is reported only when that modality is selected.

## How to Run

### 1. Install Python

Use a supported Python 3 installation.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
python app.py
```

The CLI interaction is:

```text
Select a file (Image, Text, or Audio):
image
Enter the path to the image file:
/path/to/image.png
Image result: <extracted result>
```

Replace `image` with `text` or `audio` when using another supported modality. The selected file must exist, and the corresponding processing module must be available in the checkout.

## Testing

The repository includes lightweight automated tests for the application dispatcher and its error-handling paths. The tests use mocked model components where appropriate, so they can validate application behavior without downloading large AI models.

Run the test suite with:

```bash
pytest -q
```

## Key Learning Outcomes

- Multimodal application design
- AI model integration
- Image-processing workflows
- Separation of application and image-processing logic
- Python dependency management
- Testable application interfaces and failure handling

## Future Improvements

- Add automated tests for each modality
- Document exact models and datasets used
- Add API endpoints for programmatic access
- Improve error handling for unavailable audio/camera inputs
