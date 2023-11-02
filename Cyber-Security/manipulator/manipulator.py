from PIL import Image, ImageDraw
def manipulate_image(image_path, output_path):
    with Image.open(image_path) as img:
        manipulated_img = Image.new(img.mode, img.size)
        manipulated_img.paste(img)
        red_overlay = Image.new("RGBA", img.size, (255, 0, 0, 100))
        manipulated_img = Image.alpha_composite(manipulated_img.convert("RGBA"), red_overlay)
        manipulated_img.save(output_path)
def manipulate(input_path):
 input_image_path = input_path
 output_image_path = "manipulated_image.png"
 manipulate_image(input_image_path, output_image_path)