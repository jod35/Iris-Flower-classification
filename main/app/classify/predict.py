from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np


#load the dataset
iris_dataset=load_iris()

#load the classifier
knn=KNeighborsClassifier()


#split training and testing data
X_train,X_test,y_train,y_test=train_test_split(iris_dataset['data'],
                            iris_dataset['target'],
                            random_state=0)


#fit training data within model
knn.fit(X_train,y_train)


#predict

def predict_flower_class(sp_length,sp_width,pt_length,pt_width):
    new_data=np.array(
        [[sp_length,sp_width,pt_length,pt_width]]
    )

    prediction =knn.predict(new_data)

    return prediction

