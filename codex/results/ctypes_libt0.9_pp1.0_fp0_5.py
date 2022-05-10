import ctypes
ctypes.windll.user32.MessageBoxW(0, "This program requires a resolution of 640 x 480", "Error", 1)
</code>


A:

In general, no. 
You may be able to influence the behavior of some users' browsers, by changing the colors/background colors in their browser'e options or by setting the colors/background colors in your style sheet (not sure if this will work).
Others may decide to turn images off entirely, and since your prompt is in an image, they'll never see it.
Others still will be using text-only browsers, or screen readers, or some other technological device that prevents most of your site from rendering (Braille browsers or the like).
Some users' browsers don't have images at all, or have images turned off. There is no way you will be able to display that image to them.
Finally, your prompt may appear in the wrong colors for some users. Fire up your browser in high-contrast black and white mode and see what your prompt looks like. If you don't like what you see, you can be certain that a few of your visitors won't like what they see either. 

