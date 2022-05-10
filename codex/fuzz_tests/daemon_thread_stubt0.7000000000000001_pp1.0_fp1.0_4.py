import sys, threading

def run():
	runner = unittest.TextTestRunner(verbosity=2)
	suite = unittest.TestSuite()

	# collect all the tests
	suite.addTest(unitTest.suite())
	#suite.addTest(integrationTest.suite())

	# run 'em
	runner.run(suite)

if __name__ == "__main__":
	run()
