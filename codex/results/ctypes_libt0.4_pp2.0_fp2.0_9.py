import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

window = tk.Tk()
window.title("Image Processing")
window.geometry("600x400")
window.configure(background='grey')

def get_image_path():
    path_to_image = filedialog.askopenfilename()
    return path_to_image

def get_image_name():
    return os.path.basename(get_image_path())

def get_image_extension():
    return os.path.splitext(get_image_name())[1]

def get_image_without_extension():
    return os.path.splitext(get_image_name())[0]

def get_image_folder():
    return os.path.dirname(get_image_path())

def get_image_size():
    return os.path.getsize(get_image_path())

def get_image_resolution():
    return Image.open(get_image_path()).size

def
