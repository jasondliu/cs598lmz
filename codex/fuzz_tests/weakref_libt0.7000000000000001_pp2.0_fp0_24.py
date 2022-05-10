import weakref
+
+
+class Device(db.Model):
+    id = db.Column(db.Integer, primary_key=True)
+    name = db.Column(db.String(128), index=True, unique=True)
+    description = db.Column(db.Text)
+    data = db.Column(db.Text)
+    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
+    owner = db.relationship("User", backref=db.backref("devices", lazy="dynamic"))
+
+
+class User(db.Model):
+    id = db.Column(db.Integer, primary_key=True)
+    username = db.Column(db.String(64), index=True, unique=True)
+    password = db.Column(db.String(64))
+    email = db.Column(db.String(128), index=True, unique=True)
+
+
+class Data(db.Model):
+    id = db.Column(db.Integer, primary_key=
