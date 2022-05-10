import sys, threading

def run():
   while not gtk.gdk.events_pending():
      threading.currentThread().stop_request.wait(0.02)
      if threading.currentThread().stop_request.isSet():
          return False
      while gtk.events_pending():
         gtk.main_iteration(False)


def _threaded_gtk_message(msg, title=" ", buttons=gtk.BUTTONS_OK, parent=None):
   """Display message in an asynchronous GTK message dialog.
   """
   dlg = gtk.MessageDialog(parent=parent, 
                           type=gtk.MESSAGE_INFO, 
                           buttons=buttons, 
                           message_format=msg)
   dlg.set_title(title)
   dlg.connect("response", lambda *w: dlg.destroy())
   dlg.show_all()
   gtk.threads_enter()
   gtk.main()
   gtk.threads_leave()
   del dlg
   return

class
