# Predicting the Values for Jan 2017 Stock Prices.

predicted_stock_price= regressor.predict(X_test)
predicted_stock_price = scaler.inverse_transform(predicted_stock_price)
