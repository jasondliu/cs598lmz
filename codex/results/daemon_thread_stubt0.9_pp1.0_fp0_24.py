import sys, threading

def run():
   parser = argparse.ArgumentParser(description='Return the total number of vulnerabilities by programming language and severity')
   parser.add_argument('-u','--user', help='Github username',required=True)
   parser.add_argument('-p','--password',help='Github password', required=True)
   parser.add_argument('-o','--organization',help='Github organization',required=True)
   parser.add_argument('-r','--repositories',help='Comma separated list of repositories',required=True)
   parser.add_argument('-l','--language',help='Comma separated list of programming languages, check: https://docs.trufflesuite.com/truffle/reference/contracts-and-transactions#languages',required=True)
   parser.add_argument('-s','--severitites',help='Comma separated list of severities', required=True)
   
   args = vars(parser.parse_args())
   run = Run_Test(args['user'],args['password'],args['organization'],
