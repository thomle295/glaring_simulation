import cv2
import numpy as np
import math
import random


class Glaring():

    def __init__(self, ratio_cricle_with_image=10, accelerattion=1.2,
                 pepper_noise_threshold=240, pepper_noise_percent=0.2):
        """
        The init method or constructor

        :param ratio_cricle_with_image: Define ratio of circle
            with the main image
        :param accelerattion: speed of light spread.
            (1 - (distance / radius_circle)) * ACCELERATION
        :param pepper_noise_threshold: the threshold of pixel
        :param pepper_noise_percent: noise percent in glaring in areas
        """
        self.ratio_cricle_with_image = ratio_cricle_with_image
        self.accelerattion = accelerattion
        self.pepper_noise_threshold = pepper_noise_threshold
        self.pepper_noise_percent = pepper_noise_percent

    def check_inside_circle(self, check_point, center_point_circle, radius_circle):
        """Return boolean, int

        Check the point if it is inside the circle, return that result
            and distance of checkpoint and center circle point
        """

        distance = np.linalg.norm(
            np.array(check_point) - np.array(center_point_circle))

        if (distance > radius_circle):
            return False, distance
        return True, distance

    def predict(self, image=None, image_path=None, center_circle_coordinate=None):
        try:
            img = image
            if image_path is not None:
                img = cv2.imread(image_path)
                # img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

            if img is None:
                raise ValueError("image or image_path is missing")

            img = np.asarray(img, np.float64)
            x_image, y_image, _ = img.shape
            area_image = x_image * y_image

            if center_circle_coordinate is not None:
                x_center_circle = int(center_circle_coordinate[0])
                y_center_circle = int(center_circle_coordinate[1])
                if x_center_circle > x_image or y_center_circle > y_image:
                    raise ValueError(
                        "x-coordinate or y-coordinate is larger than image")
            else:
                x_center_circle = int(np.random.uniform(x_image))
                y_center_circle = int(np.random.uniform(y_image))

            area_circle = int(area_image / self.ratio_cricle_with_image)
            radius_circle = int(math.sqrt(area_circle / math.pi))
            # diameter_circle = radius_circle * 2

            sub_image_x1 = (
                x_center_circle - radius_circle
                ) if (x_center_circle - radius_circle) > 0 else 0
            sub_image_x2 = (
                x_center_circle + radius_circle
                ) if (x_center_circle + radius_circle) <= x_image else x_image
            sub_image_y1 = (
                y_center_circle - radius_circle
                ) if (y_center_circle - radius_circle) > 0 else 0
            sub_image_y2 = (
                y_center_circle + radius_circle
                ) if (y_center_circle + radius_circle) <= y_image else y_image

            for x in range(sub_image_x1, sub_image_x2):
                for y in range(sub_image_y1, sub_image_y2):
                    check_inside_circle_result, distance = self.check_inside_circle(
                        (x, y),
                        (x_center_circle, y_center_circle),
                        radius_circle
                    )

                    if check_inside_circle_result is not True:
                        continue

                    difference_current_pixel_to_max = 256 - img[x, y]
                    ratio = (1 - (distance / radius_circle)) * \
                        self.accelerattion
                    new_pixel = ratio * difference_current_pixel_to_max
                    new_pixel = img[x, y] + new_pixel

                    if (new_pixel.mean() < self.pepper_noise_threshold) \
                            and (np.random.uniform(10) < self.pepper_noise_percent):
                        continue

                    img[x, y] = new_pixel

            return img.astype(int)
        except ValueError:
            raise
        pass
