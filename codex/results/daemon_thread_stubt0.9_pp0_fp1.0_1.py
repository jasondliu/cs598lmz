import sys, threading

def run():
    bestscores = []
    
    logger.info("Starting")
    
    while not close:
        while len(taskcache) == 0 and not close:
            time.sleep(0.25)
        
        if close:
            break
        
        # Obtain a new task
        t = taskcache.pop(0)
        
        try:
            logger.debug("Starting task %d." % t.id)
            
            # Run the task
            t.run()
            
            # Update information about who's best
            bestscores.append(t.incumbent)
            currentbest = np.min(bestscores)
            logger.info("Task %d finished. Best score: %f" % (t.id, currentbest))
            
            # Record the best individual
            if t.incumbent == currentbest:
                with open(picklefile, 'w') as f:
                    pickle.dump(t.bestindividual, f)
        except Exception as e:
            logger.error("Task %d could not be finished." % t.id)
