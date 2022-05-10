import threading
threading.Thread(target=realtime_plot).start()
 
app.run(host="0.0.0.0") # ローカルからもアクセスできるようにする!

time.sleep(10)

print("preparing to stop the plotter")
plotStop = True

