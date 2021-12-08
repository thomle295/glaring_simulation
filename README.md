## The Augmentation methods: this lib help simulation glaring phenomena in image

## Install:
```
pip3 install glaring-simulation
```

## Basic using:
```
from glaring_simulation import Glaring
glaring_testing = Glaring.Glaring()
img_path = "resource/image.jpg"
glaring_image = glaring_testing.predict(image_path=img_path)
cv2.imwrite("resource/glaring_image.jpg", glaring_image)
```

### Normal image
![Normal image](/resource/image.jpg)

### Glaring image
![Glaring image](/resource/glaring_image.jpg)
