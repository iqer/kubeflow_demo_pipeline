import joblib
import tensorflow as tf
import argparse
import pickle


def train_model(x_train, y_train, model_dir):
    x_train_data = pickle.load(x_train)
    y_train_data = pickle.load(y_train)
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x_train_data, y_train_data, epochs=5)

    joblib.dump(model, '{}/model.pickle'.format(model_dir))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_train')
    parser.add_argument('--y_train')
    parser.add_argument('--model_dir')
    args = parser.parse_args()
    train_model(args.x_train, args.y_train, args.model_dir)
