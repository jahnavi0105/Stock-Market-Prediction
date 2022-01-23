#Preparing the Input for the Model.

dataset_total= pd.concat((dataset_train[ 'Open'], dataset_test['Open']), axis = 0)
inputs = dataset_total[len (dataset_total)- len(dataset_test)-60:].values
inputs inputs.reshape (-1,1)
inputs = scaler.transform(inputs)
X_test= []
for i in range (60,80):

    X_test.append(inputs [i-60:i, 0])
    X_test = np.array(X_test)
    X_test = np.reshape (X_test, (X_test.shape [0], X_test.shape [1], 1))
