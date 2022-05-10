import threading
threading.stack_size(2**27)  # Increase thread stack size

#declares handlers for our AWS api gateway authorizer
def create_summary_handler(event='', context=''):
	return create_summary(event)

def get_summary_handler(event='', context=''):
	return get_summary(event)

def lambda_handler(event, context):
	#main entry point for lambda
	#tells it what to run and then immediately runs the compiled lambda 
    lambdas = {
        'get_summary': get_summary_handler,
        'create_summary': create_summary_handler
    }
    return lambdas[event['lambda']](event, context)
