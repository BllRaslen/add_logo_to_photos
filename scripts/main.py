from PIL import Image
import os


def add_logo_to_photos(folder_path, logo_path, output_folder, logo_size):
    # Open the logo image and convert it to RGBA format
    logo = Image.open(logo_path).convert("RGBA")

    # Resize the logo
    logo = logo.resize(logo_size)

    # Iterate through all photos in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith((".jpg", ".jpeg", ".png", ".webp")):
            # Open the photo
            photo_path = os.path.join(folder_path, filename)
            photo = Image.open(photo_path)

            # Calculate the position to paste the logo at the center
            position = ((photo.width - logo.width) // 2, (photo.height - logo.height) // 2)

            # Paste the logo onto the photo
            photo.paste(logo, position, logo)

            # Save the edited photo with the same format as the original
            output_path = os.path.join(output_folder, filename)
            photo.save(output_path, format=photo.format)

            # Close the photo
            photo.close()

    # Close the logo
    logo.close()


# Usage example
folder_path = "C:\\Users\\bilal\\OneDrive\\Desktop\\fotos"
logo_path = "C:\\Users\\bilal\\OneDrive\\Desktop\\fotos\\logo.png"
output_folder = "C:\\Users\\bilal\\OneDrive\\Desktop\\out"
logo_size = (100, 100)  # Specify the desired logo size (width, height)

add_logo_to_photos(folder_path, logo_path, output_folder, logo_size)
