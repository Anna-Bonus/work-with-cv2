import cv2 as cv
import sys, os, copy

class DontExistPath(Exception):
    pass


class WrongQuantityOfArguments(Exception):
    pass


class NotTheImage(Exception):
    pass


CASCADE_XML_FILENAME = "lbpcascade_frontalface.xml"
LINE_WIDTH = 5
SCALE_FACTOR = 1.1
MIN_NEIGHBORS = 5
MIN_SIZE = (40, 40)
BGR_IDENTIFIER = (255, 0, 0)
cascade = cv.CascadeClassifier(CASCADE_XML_FILENAME)


def detect_faces_on_image(input_image):
    image_copy = copy.copy(input_image)
    try:
        gray_image = cv.cvtColor(image_copy, cv.COLOR_BGR2GRAY)  # it is necessary for better recognition of faces
    except:
        raise NotTheImage('Can\'t convert file to gray for detecting faces')
    #cascade = cv.CascadeClassifier(CASCADE_XML_FILENAME)
    rects = cascade.detectMultiScale(gray_image, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS, minSize=MIN_SIZE, flags=cv.CASCADE_SCALE_IMAGE)
    for x, y, w, h in rects:
        cv.rectangle(image_copy, (x, y), (x+w, y+h), BGR_IDENTIFIER, LINE_WIDTH)
    return image_copy


def detect_faces_on_file(input_name, output_name):
    image = cv.imread(input_name)
    if image is None:
        print 'Can\'t open file', input_name, 'as image'
    else:
        result = detect_faces_on_image(image)
        cv.imwrite(output_name, result)

def detect_faces_in_folder(in_folder, out_folder):
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    for name_file in os.listdir(in_folder):
        path_in = os.path.join(in_folder, name_file)
        path_out = os.path.join(out_folder, name_file)
        try:
            detect_faces_on_file(path_in, path_out)
        except NotTheImage as e:
            print(e.message)

if sys.argv[1] == '--help':
    print 'Please, enter two arguments: <source> <output> after', sys.argv[0], 'for detect faces in source and save in output'
    exit()
if len(sys.argv) == 3:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    if os.path.exists(input_path):
        try:
            if os.path.isdir(input_path):
                detect_faces_in_folder(input_path, output_path)
            else:
                detect_faces_on_file(input_path, output_path)
        except NotTheImage:
            print('VSE OCHEN PLOHO')
    else:
        raise DontExistPath('This path', input_path, 'does not exist')
else:
    raise WrongQuantityOfArguments('Please, enter two arguments: <source> <output>')




"""
def detect_faces(name_image, save_path):
    image_in = cv.imread(name_image)
    if image_in is None:
        print 'Can\'t open image'
        exit()
    image_copy = copy.copy(image_in)
    try:
        gray_image = cv.cvtColor(image_copy, cv.COLOR_BGR2GRAY)
    except:
        # raise Exception('Can\'t convert image to gray: ', cv.error)
        raise NotTheImage('Can\'t convert file', name_image, 'to gray for detecting faces')
    cascade = cv.CascadeClassifier(CASCADE_XML_FILENAME)
    #rects = cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40), flags=cv.CASCADE_SCALE_IMAGE)
    rects = cascade.detectMultiScale(gray_image, scaleFactor=SCALE_FACTOR, minNeighbors=MIN_NEIGHBORS, minSize=MIN_SIZE, flags=cv.CASCADE_SCALE_IMAGE)
    for x, y, w, h in rects:
        cv.rectangle(image_copy, (x, y), (x+w, y+h), BGR_IDENTIFIER, LINE_WIDTH)
    cv.imwrite(save_path, image_copy)

#detect_faces(sys.argv[1], sys.argv[2])

def detect_faces_in_folder(in_folder, out_folder):
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    for name_file in os.listdir(in_folder):
        path_in = os.path.join(in_folder, name_file)
        path_out = os.path.join(out_folder, name_file)
        try:
            detect_faces(path_in, path_out)
        except NotTheImage as e:
            print(e.message)

if len(sys.argv) == 3:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    #input_path = "image1.jpg"
    #output_path = "resultik.jpg"
    if os.path.exists(input_path):
        try:
            if os.path.isdir(input_path):
                detect_faces_in_folder(input_path, output_path)
            else:
                detect_faces(input_path, output_path)
        except NotTheImage:
            print('VSE OCHEN PLOHO')
    else:
        raise DontExistPath('This path', input_path, 'does not exist')
else:
    raise WrongQuantityOfArguments('Please, enter two arguments: <source> <output>')
"""