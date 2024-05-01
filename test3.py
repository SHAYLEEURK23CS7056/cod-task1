from PIL import Image
from PIL import ImageFilter

def display_image(img):
    img.show()

def image_to_grayscale(img):
    return img.convert("L")

def print_image_size(img):
    print("Image size:", img.size)

# Load the image
img = Image.open("example.jpg")

# Display the image
display_image(img)

# Convert the image to grayscale
img = image_to_grayscale(img)

# Display the image again
display_image(img)

# Print the image size
print_image_size(img)

# Resize the image to half
img = img.resize((int(img.width / 2), int(img.height / 2)))

# Display the image
display_image(img)

# Rotate the image by 145 degrees
img = img.rotate(145)

# Display the image
display_image(img)

# Resize the image by 50 units in x and 70 units in y
img = img.resize((img.width + 50, img.height + 70))

# Display the image
display_image(img)

# Flip the image horizontally
img = img.transpose(Image.FLIP_LEFT_RIGHT)

# Display the image
display_image(img)

# Flip the image vertically
img = img.transpose(Image.FLIP_TOP_BOTTOM)

# Display the image
display_image(img)

# Crop the image
img = img.crop((0, 0, img.width / 2, img.height / 2))

# Display the image
display_image(img)

# Threshold the image and convert it to binary
img = img.point(lambda x: 0 if x < 128 else 255, "1")

# Display the image
display_image(img)

# Apply the blur filter
img = img.filter(ImageFilter.BLUR)

# Display the image
display_image(img)