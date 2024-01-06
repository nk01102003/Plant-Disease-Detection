
import warnings
warnings.filterwarnings('ignore')

import tensorflow as tf 
classifierLoad = tf.keras.models.load_model('model.h5')

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('./Data/Apple___Black_rot/30aebb07-bde6-44c8-bee2-a06ff42a948d___JR_FrgE.S 3071.JPG', target_size = (200, 200))

test_image = np.expand_dims(test_image, axis=0)
print(test_image)
result = classifierLoad.predict(test_image)
print(result)
out=''
fer =""
if result[0][0] == 1:

    out = "Apple___Black_rot"
    fer = 'Griffin  Fertilizer  reducing the fungus'

elif result[0][1] == 1:

    out = "Apple___healthy"

elif result[0][2] == 1:
    out = "Corn_(maize)___healthy"

elif result[0][3] == 1:
    out = "Corn_(maize)___Northern_Leaf_Blight"
    fer = 'Griffin  Fertilizer  reducing the fungus'

elif result[0][4] == 1:
    out = "Peach___Bacterial_spot"
    fer = 'Compounds available for use on peach and nectarine for bacterial spot include copper, oxytetracycline (Mycoshield and generic equivalents), and syllit+captan; however, repeated applications are typically necessary for even minimal disease control.'

elif result[0][5] == 1:
    out = "Peach___healthy"

if result[0][6] == 1:

    out = "Pepper_bell___Bacterial_spot"

    fer = 'Seed treatment with hot water, soaking seeds for 30 minutes in water pre-heated to 125 F/51 C, is effective in reducing bacterial populations on the surface and inside the seeds'

elif result[0][7] == 1:

    out = "Pepper_bell___healthy"

elif result[0][8] == 1:
    out = "Potato___Early_blight"
    fer = 'Griffin  Fertilizer  reducing the fungus'

elif result[0][9] == 1:
    out = "Potato___healthy"
    fer = 'Griffin  Fertilizer  reducing the fungus'

elif result[0][10] == 1:
    out = "Potato___Late_blight"
    fer = 'Griffin  Fertilizer  reducing the fungus'

elif result[0][11] == 1:
    out = "Tomato___Bacterial_spot"
    fer = 'Griffin  Fertilizer  reducing the fungus'

elif result[0][12] == 1:
    out = "Tomato___Late_blight"
    fer = 'Spraying fungicides is the most effective way to prevent late bligh'

elif result[0][13] == 1:
    out = "Tomato___Leaf_Mold"
    fer = 'Griffin  Fertilizer  reducing the fungus'

elif result[0][14] == 1:
    out = "Tomato___Septoria_leaf_spot"
    fer = 'Griffin  Fertilizer  reducing the fungus'




print(out)
print(fer)