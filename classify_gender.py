# import necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import cv2


def funwithimage(image_directory):

    # read input image
    image = cv2.imread(image_directory)

   # if image is None:
    #    print("Could not read input image")
     #   exit()

    # preprocessing
    output = np.copy(image)
    image = cv2.resize(image, (96,96))
    image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    # load pre-trained model
    model = load_model("gender_classification.model")

    # run inference on input image
    confidence = model.predict(image)[0]

    # write predicted gender and confidence on image (top-left corner)
    classes = ["man", "woman"]
    idx = np.argmax(confidence)
    label = classes[idx]
    label = "{}: {:.2f}%".format(label, confidence[idx] * 100)
    
   

#    cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
#                    0.7, (0, 255, 0), 2)
#
#    # print confidence for each class in terminal
#    print("d:\s.jpg")
#    print(classes)
#    print(confidence)
#
#    # display output image
#    cv2.imshow("Gender classification", output)
#
#    # press any key to close image window
#    cv2.waitKey()
#
    # save output image
    #cv2.imwrite("gender-classification.jpg", output)
    print (label)
    return label
#
#    # release resources
#    cv2.destroyAllWindows()
