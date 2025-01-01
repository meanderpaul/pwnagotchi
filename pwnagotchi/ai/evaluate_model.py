import tensorflow as tf
from sklearn.metrics import accuracy_score
from google.protobuf import text_format


def evaluate_model(model_path, test_data_path):
    # Load test data
    test_data = pd.read_csv(test_data_path)
    test_features = test_data.drop('label', axis=1)
    test_labels = test_data['label']
    
    # Load model
    model = tf.keras.models.load_model(model_path)
    
    # Make predictions
    predictions = model.predict(test_features)
    predicted_labels = np.argmax(predictions, axis=1)
    
    # Evaluate model performance
    accuracy = accuracy_score(test_labels, predicted_labels)
    print(f"Model accuracy: {accuracy}")

if __name__ == "__main__":
    evaluate_model("updated_model.h5", "test_data.csv")
