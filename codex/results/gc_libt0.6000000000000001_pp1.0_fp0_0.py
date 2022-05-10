import gc, weakref, threading
			self.weakrefs = weakref.WeakKeyDictionary()
			def weak_ref_callback(ref):
				print "weak_ref_callback"
				self.weakrefs.pop(ref.key)
				self.weakrefs_lock.release()
			self.weakrefs_lock = threading.Lock()

			self.weakrefs_lock.acquire()
			self.weakrefs[obj] = weakref.ref(obj, weak_ref_callback)
			self.weakrefs_lock.release()
			gc.collect()
			self.weakrefs_lock.acquire()
			assert obj not in self.weakrefs
			self.weakrefs_lock.release()
			print "weak ref test: success"
		except:
			print "weak ref test: failure"
			print_exc()
			self.weakrefs = None

		self.picture
