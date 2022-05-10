import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# set up the window
root = tk.Tk()
root.title('Media Player')
root.minsize(600, 400)

# set up the player
player = tk.StringVar()
player_frame = ttk.Frame(root)
player_frame.pack(side=tk.TOP)
video_player = tk.Label(player_frame)
video_player.pack(side=tk.TOP)

# set up the play/pause button
play_button = ttk.Button(player_frame, text='Pause',
                        command=lambda: toggle_video_state())
play_button.pack(side=tk.TOP)

# set up the slider
slider_frame = ttk.Frame(player_frame)
slider_frame.pack(side=tk.TOP)
