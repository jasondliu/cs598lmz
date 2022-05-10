import ctypes
ctypes.windll.user32.SetProcessDPIAware()
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('config_file', type=str, help='the config file path')
parser.add_argument('--gui', action='store_true', default=True, help='use gui')
first_arg = parser.parse_args().config_file
config_path = Path(first_arg).absolute()
config = Config(config_path)
fileio = FileIO(config)

plt.rcParams["figure.max_open_warning"] = 0

# create gui
app = gui.App(config, fileio, fileio.get_file_names())
app.mainloop()
app.destroy()

if config.record_video:
    os.system(f'cd {config.record_path} && ffmpeg -f image2 -r 24 -i _%8d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p result.mp4')
