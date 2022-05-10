import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# ------------------------------------------------------------
#
# Job configuration
#
# ------------------------------------------------------------

## The type of the application: <Application>.
sct.printv('\nJob type: segmentation (sct_deepseg_sc)', verbose)

## The path to the template file that contains the default values.
path_template = os.path.join(p.folder_templates, p.file_template_sc)

## The path to the template file that contains the default values.
path_template_warp = os.path.join(p.folder_templates, p.file_template_sc_warp)

## The path to the template file that contains the default values for the warping of the labels.
path_template_warp_labels = os.path.join(p.folder_templates, p.file_template_sc_warp_labels)

## The path to the template file that contains the default values for spinal cord detection.
