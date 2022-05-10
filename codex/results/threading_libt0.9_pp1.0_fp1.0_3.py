import threading
threading.stack_size(32768*16)


def add_text_to_image(img, text, position):
    """Creates a black image with text on it and adds it to the given image."""
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    thickness = 3
    text_size = cv2.getTextSize(text, font, font_scale, thickness)
    text_img = np.zeros((text_size[0][1], text_size[0][0], 3), dtype=np.uint8)

    # Text background.
    bg_pt0 = (0, text_size[0][1])
    bg_pt1 = (text_size[0][0], 0)
    cv2.rectangle(text_img, bg_pt0, bg_pt1, color=(0, 0, 0), thickness=-1)

    # Text foreground.
    fg_pt0 = (0, text_size[0][1] - int(0.25 * text_
