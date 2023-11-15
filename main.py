import os
from PIL import Image

def pixelate(input_path, output_folder, pixel_size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the image
    img = Image.open(input_path)

    # Get image size
    width, height = img.size

    # Resize the image to a small size
    img = img.resize((width // pixel_size, height // pixel_size), resample=Image.NEAREST)

    # Resize the small image back to the original size
    img = img.resize((width, height), resample=Image.NEAREST)

    # Build the output path with autorenaming
    output_path = os.path.join(output_folder, f"pixelated_{os.path.basename(input_path)}")

    # Save the pixelated image
    img.save(output_path)

if __name__ == "__main__":
    # Input path
    input_folder = "input_images"

    # Output folder (will be created if it doesn't exist)
    output_folder = "pixelated_images"

    # Pixel size (adjust this to control the level of pixelation)
    pixel_size = 10

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            pixelate(input_path, output_folder, pixel_size)

    print("Pixelation complete. Check the output folder:", output_folder)
