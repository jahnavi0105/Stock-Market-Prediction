# Building the Model by Importing the Crucial Librari Adding Different Layers    

from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
regressor = Sequential()
regressor.add (LSTM (units = 50, return_sequences= True, input_shape= (X_train.shape[1],1)))
regressor.add(Dropout(0.2))
regressor.add (LSTM (units = 50, return_sequences= True))
regressor.add(Dropout(0.2))
regressor.add(LSTM (units = 50, return_sequences= True)) 
regressor.add(Dropout (0.2))    
regressor.add(LSTM(units=50))
regressor.add(Dropout(0.2))    
regressor.add(Dense (units=1))
