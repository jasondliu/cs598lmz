import ctypes
ctypes.windll.user32.LockWorkStation()"""
            else:
                lock_command = "gnome-screensaver-command -a"
            os.popen(lock_command)

        def lock_screen_handle(self):
            """Lock the screen with a password verification dialog

            bumblebee-status will run a specified command, which is
            responsible for showing the password dialog, then the
            lock screen will be locked (unless the password was
            entered wrong)
            """
            if self._interval is not None:
                self._timer.cancel()
                self._run_interval()

            cmd = self._module.parameter("command-lock-screen")
            exit_code = subprocess.call(cmd)
            if exit_code == 0:
                LockScreenCommand(self._module).run()

        def run(self):
            timestamp = time.strftime("%s", time.localtime())
            if self._lastrun < timestamp:
                self._lastrun = timestamp
                lock_screen_handle(self)

    run = LockCommand()
