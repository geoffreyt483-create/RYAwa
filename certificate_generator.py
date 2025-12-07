from PIL import Image, ImageDraw, ImageFont

def generate_certificate(name, workshop):
    template = Image.open("static/certificate_template.png")
    draw = ImageDraw.Draw(template)

    font = ImageFont.truetype("static/fonts/Roboto-Bold.ttf", 60)
    draw.text((600, 500), name, font=font, fill="black")

    output_path = f"certificates/{name}_{workshop}.png"
    template.save(output_path)

    return output_path
