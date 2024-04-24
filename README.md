# Add Logo to Photos

This Python script allows you to add a logo to multiple photos within a specified folder. It finds all photos in the folder (with supported formats: .jpg, .jpeg, .png, .webp) and adds the logo to each photo, positioning it at the center. The edited photos are saved in an output folder while maintaining their original format.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies using pip:
`pip install Pillow
`

## Usage

1. Import the `add_logo_to_photos` function from the script.
2. Specify the folder path containing the photos (`folder_path`).
3. Specify the path to the logo image (`logo_path`).
4. Specify the output folder where the edited photos will be saved (`output_folder`).
5. Specify the desired logo size (`logo_size`).
6. Call the `add_logo_to_photos` function with the specified parameters.

Example usage:

```python
from PIL import Image
import os

def add_logo_to_photos(folder_path, logo_path, output_folder, logo_size):
 # Your implementation here

# Usage example
folder_path = "path/to/photos/folder"
logo_path = "path/to/logo/image"
output_folder = "path/to/output/folder"
logo_size = (100, 100)  # Specify the desired logo size (width, height)

add_logo_to_photos(folder_path, logo_path, output_folder, logo_size)
```
**Replace "path/to/photos/folder", "path/to/logo/image", and "path/to/output/folder" with your actual paths.**
## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

**Make sure to replace `"path/to/photos/folder"`, `"path/to/logo/image"`, and `"path/to/output/folder"` with the actual paths where your photos, logo, and output folder are located.**




