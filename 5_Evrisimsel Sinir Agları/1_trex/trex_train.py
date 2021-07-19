import glob #glob ve os ile resimlerimize klasörlerimize erişim sağlayacağız
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
# keras kütüphanesini kullanarak derin öğrenme algoritmamızın
# tasarlanması ve eğitimini gerçekleştireceğiz

# dense:bizim fu connected layerimizda bulunan katmandı
# dropout: seyreltme
# Flatten: Düzleştirme
# Conv2D: evrişim ağımız
# MaxPooling2D: piksel ekleme kavramı
from PIL import Image
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

imgs = glob.glob("./img_nihai/*.png")

width = 125
height = 50

X = []
Y = []

for img in imgs:
    
    filename = os.path.basename(img)
    label = filename.split("_")[0]
    im = np.array(Image.open(img).convert("L").resize((width, height)))
    im = im / 255
    X.append(im)
    Y.append(label)
    
X = np.array(X)
X = X.reshape(X.shape[0], width, height, 1) #burada kaç tane resim olduğunu yazıyoruz. buraya 1 yazmamızın nedeni keras buraya herhangi bir şey yazmamızı istiyor
# ve resmimizi siyah beyaz kullanacağız.

# sns.countplot(Y) #y den kaç tane var görselleştiriyoruz

def onehot_labels(values):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    onehot_encoder = OneHotEncoder(sparse = False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded),1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    return onehot_encoded

Y = onehot_labels(Y)
train_X, test_X, train_y, test_y = train_test_split(X, Y , test_size = 0.25, random_state = 2)    

# cnn model
model = Sequential()   
model.add(Conv2D(32, kernel_size = (3,3), activation = "relu", input_shape = (width, height, 1)))
model.add(Conv2D(64, kernel_size = (3,3), activation = "relu"))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation = "relu"))
model.add(Dropout(0.4))
model.add(Dense(3, activation = "softmax")) #çıktı fonk. softmax i 2 den fazla çıktı varsa kullanıyoruz

# if os.path.exists("./trex_weight.h5"):
#     model.load_weights("trex_weight.h5")
#     print("Weights yuklendi")    

model.compile(loss = "categorical_crossentropy", optimizer = "Adam", metrics = ["accuracy"])#loss nihai olarak hatamızı bulmamızı sağlıyor. geriye doğru türev alma işlemi yapıyoruz. loss çok az ise bizim modelimiz iyi eğitilmiş oluyor

model.fit(train_X, train_y, epochs = 35, batch_size = 64) # epochs: resimlerimizin hepsinin toplamda kaç kez eğitileceği, batch_size ise: resimlerimizin kaç grup halinde iterasyona sokulacağını belirtiyor

score_train = model.evaluate(train_X, train_y)
print("Eğitim doğruluğu: %",score_train[1]*100) #skorun 0. indexi bana kaybı 1. indexi ise accuracy getiriyor   
    
score_test = model.evaluate(test_X, test_y)
print("Test doğruluğu: %",score_test[1]*100)      
    
 
open("model_new.json","w").write(model.to_json())
model.save_weights("trex_weight_new.h5")   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    