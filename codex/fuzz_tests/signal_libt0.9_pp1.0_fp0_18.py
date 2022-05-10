import signal
signal.signal(signal.SIGINT, signal.default_int_handler)

s = Server(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        ".testing.db"), listen_port=8080, listen_ip="127.0.0.1")

# Insert a row and test
c = s.connection
print c(), "New user created."
time.sleep(3)
print c.insert(
    """\
    INSERT INTO tblClass (ClassID, CurriculumID, SID, Section, ClassTitle)
    VALUES
    (?, ?, ?, ?, ?)""",
    (
        1, 1, 2, 0, 'My class title'
    )
)

# Update a row and test
print c.update(
    """\
    UPDATE tblClass SET ClassTitle = ? WHERE ClassID = ?""",
    'My new class title',
    1
)
print
print 'Testing join query'
print
print c.query(
    """\
    SELECT *
