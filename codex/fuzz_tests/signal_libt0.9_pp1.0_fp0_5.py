import signal
signal.signal(signal.SIGINT, signal_handler)

# Initialize NT service interface
if options.isService:
    ntService = ntservice.NTService(serviceName='mod-injector', displayName='mod_injector')
    ntService.recovery = True
    ntService.recoveryOptions = ['Restart', 'Restart', 'Restart']
    ntService.recoveryActions = [(600, 0), (300, 0), (0, 30)]
    ntService.setParameters(version, version)

# Configure type of service and run
if options.isService:
    ntService.run(injector)
else:
    try:
        injector.runForever()
    except KeyboardInterrupt:
        exit(0)
