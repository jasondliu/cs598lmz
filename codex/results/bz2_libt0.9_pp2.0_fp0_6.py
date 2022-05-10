import bz2
bz2_btn = tk.Button(root, text="bz2 compression")
bz2_btn.config(command=lambda:compress('bz2', bz2))
bz2_btn.pack()

root.mainloop()
</code>

