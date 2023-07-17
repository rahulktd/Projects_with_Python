from rembg import remove
from PIL import Image

input_path = "bird-thumbnail.jpg"
output_path = "bird-thumbnail.png"
inp = Image.open(input_path)
out = remove(inp)
out.save(output_path)