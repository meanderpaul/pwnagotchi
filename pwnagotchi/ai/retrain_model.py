import tensorflow as tf

def retrain_model(input_path, model_path):
    # Load preprocessed data
    data = pd.read_csv(input_path)
    train_data = data.drop('label', axis=1)
    train_labels = data['label']
    
    # Load existing model
    model = tf.keras.models.load_model(model_path)
    
    # Retrain model
    model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_split=0.2)
    
    # Save updated model
    model.save("updated_model.h5")

if __name__ == "__main__":
    retrain_model("preprocessed_data.csv", "handshake_model.h5")
