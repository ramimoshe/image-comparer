import cv2
from urllib.request import urlopen
import numpy as np

OPENCV_METHODS = {
    "Correlation": cv2.HISTCMP_CORREL,  # output range: 0-1 higher is better
    "Chi-Squared": cv2.HISTCMP_CHISQR,  # output range: 0-INF lower is better
    "Intersection": cv2.HISTCMP_INTERSECT,  # output range: 0-INF higher is better
    "Hellinger": cv2.HISTCMP_BHATTACHARYYA  # output range: 0-1 lower is better
}


def __url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image


def __compare_images(method, image1, image2):
    # extract a 3D RGB color histogram from the image,
    # using 8 bins per channel, normalize
    hist = cv2.calcHist([image1], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    image1Hist = cv2.normalize(hist, hist).flatten()
    hist = cv2.calcHist([image2], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    image2Hist = cv2.normalize(hist, hist).flatten()

    return cv2.compareHist(image1Hist, image2Hist, method)


def compare(method_name, image_url1, image_url2):
    method = OPENCV_METHODS.get(method_name)
    if method is None:
        raise Exception("UNKNOWN_IMAGE_COMPARER_METHOD")

    return __compare_images(
        method,
        __url_to_image(image_url1),
        __url_to_image(image_url2)
    )
