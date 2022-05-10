import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H"),daemon=True).start()
########################################################################################################################

while(True): # Loop until run == False
    for event in pygame.event.get():
        if (event.type == QUIT): # If the window was closed, end
            run = False
            break

        if (event.type == pygame.KEYDOWN): # If a key was pressed
            if(event.key == pygame.K_ESCAPE):  # End if escape was selected
                run =  False
                break
            handleEvent(event)
        handleMiscEvents(event)
    #    if (event.key == pygame.K_SPACE):       # If space was pressed, make a button
    #        handleClick(event)

    update()
    #drawButtons()
    draw()
    clock.tick(25) # set fps

pygame.quit()
