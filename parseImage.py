from tqdm import tqdm
import argparse
import cv2

parser = argparse.ArgumentParser(
                    prog='ImageParser',
                    description='Converts images to a script that can display them on a TI Nspire calculator')
parser.add_argument("-i", "--input")
parser.add_argument("-o", "--output", nargs="?", const="output.lua")
parser.add_argument("-s", "--size", nargs="?", const="200x200")
args = parser.parse_args()

image_resolution = []
for scale in args.size.split("x"):
    image_resolution.append(int(scale))

code_lines = []

def add_pixel(r, g, b):
    global code_lines
    code_lines.append("{" + f"{r},{g},{b}" + "},")

def process_image(img_path):
    image = cv2.imread(img_path)

    image = cv2.resize(image, image_resolution)

    size_y = image.shape[0]
    size_x = image.shape[1]

    for y in tqdm(range(0,size_y)):
        for x in range(0,size_x):
            pixel_rgb = image[y][x]
            add_pixel(pixel_rgb[2], pixel_rgb[1], pixel_rgb[0])


    write_code()

def write_code():
    global code_lines
    code_string = '\n'.join(code_lines)
    with open(args.output, "w") as f:
        f.write("local pixels =  {")
        f.write(code_string)
        f.write("}\n")

        f.write("function on.paint(gc)\n")
        f.write("local pixels_curr = 1\n")
        f.write(f"for j=0,{image_resolution[-1]-1} do\n")
        f.write(f"for i=0,{image_resolution[0]-1} do\n")
        f.write("gc:setColorRGB(unpack(pixels[pixels_curr]))\n")
        f.write("gc:fillRect(i,j,1,1)\n")
        f.write("pixels_curr = pixels_curr + 1\n")
        f.write("end\n")
        f.write("end\n")
        f.write("end")

if __name__ == "__main__":
    process_image(args.input)

