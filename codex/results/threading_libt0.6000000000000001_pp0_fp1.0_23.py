import threading
threading.Thread(target=self.check_for_button).start()
</code>
Then you can check for the button in the <code>check_for_button</code> method:
<code>def check_for_button(self):
    while True:
        if self.button.isChecked():
            print "button is checked"
        time.sleep(1)
</code>

