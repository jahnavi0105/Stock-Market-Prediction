#Creating x_train and y_train data structures

X_train = []
y_train  = []
for i in range (60,1258):

    X_train.append(scaled_training_set[i-60:1, 0])
    y_train.append(scaled_training_set[i, 0])
X_train = np.array(X_train)
y_train = np.array(y_train)
