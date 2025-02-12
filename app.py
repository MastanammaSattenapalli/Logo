from PIL import Image, ImageDraw, ImageFont
import random
import colorsys

def generate_logo(flavor_theme, output_filename="logo.png"):
    """
    Generates a simple logo based on a flavor theme.

    Args:
        flavor_theme:  A string describing the flavor (e.g., "Tropical", "Minty Fresh", "Spicy").
        output_filename: The name of the file to save the logo to (e.g., "logo.png").
    """

    width = 500
    height = 300
    image = Image.new("RGB", (width, height), "white")  # Background color
    draw = ImageDraw.Draw(image)

    # --- Color Palette ---
    if flavor_theme.lower() == "tropical":
        colors = ["#FFD700", "#FFA07A", "#3CB371"] # Gold, LightSalmon, MediumSeaGreen

    elif flavor_theme.lower() == "minty fresh":
        colors = ["#98FF98", "#E0FFFF", "#FFFFFF"]  # PaleGreen, LightCyan, White

    elif flavor_theme.lower() == "spicy":
        colors = ["#FF4500", "#FFA07A", "#A52A2A"] # Orangered, LightSalmon, Brown

    else:  # Default Palette
        colors = ["#ADD8E6", "#87CEEB", "#4682B4"]  # LightBlue, SkyBlue, SteelBlue

    # --- Logo Elements ---

    # 1. Background Shape
    shape_color = random.choice(colors)
    draw.rectangle([(0, 0), (width, height)], fill=shape_color) # full background rectangle


    # 2. Central Circle
    circle_color = random.choice([c for c in colors if c != shape_color]) # Different than background
    circle_x = width // 2
    circle_y = height // 2
    circle_radius = min(width, height) // 4
    draw.ellipse((circle_x - circle_radius, circle_y - circle_radius,
                circle_x + circle_radius, circle_y + circle_radius),
               fill=circle_color, outline="black")

    # 3. Text (Simple)
    text_color = "black" if circle_color != "black" else "white" # Adjust text color
    font_size = 30
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Replace "arial.ttf" with the actual font path if needed
    except IOError:
        font = ImageFont.load_default()  # Use default if Arial not found

    text = flavor_theme.upper() # just use flavor theme as text for now
    text_width, text_height = draw.textsize(text, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # --- Save the Image ---
    image.save(output_filename)
    print(f"Logo saved as {output_filename}")

# --- Example Usage ---
flavor = input("Enter a flavor theme: ")  # e.g., "Tropical", "Minty Fresh", "Spicy"
generate_logo(flavor, "my_logo.png")