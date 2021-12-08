from glaring_simulation.Glaring import *
import os
import cv2


def test_glaring_random():
    glaring_testing = Glaring()
    img_path = "resource/image.jpg"
    glaring_image = glaring_testing.predict(image_path=img_path)
    # glaring_image = cv2.cvtColor(glaring_image, cv2.COLOR_RGB2BGR)
    cv2.imwrite("resource/glaring_image.jpg", glaring_image)
    assert os.path.isfile("resource/glaring_image.jpg") is True
