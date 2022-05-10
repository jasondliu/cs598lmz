import sys, threading

def run():
    global data
    data = subprocess.check_output(["git", "status"], universal_newlines=True)

def update():
    threading.Thread(target=run).start()

def draw(p, width, height):
    global data
    if data:
        p.fill(0)
        p.text(data, 0, 0, width, height, monoBitmap=True, spacing=1, align=uiconstants.LEFT)

def load_font(font_name):
    font_path = os.path.join(os.path.dirname(__file__), font_name)
    return ImageFont.load(font_path)

def main():
    image = Image.new("1", (128, 64))
    draw(image.
