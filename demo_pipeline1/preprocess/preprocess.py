from tensorflow import keras
import argparse
import os
import pickle


def preprocess(data_dir):
    fashion_mnist = keras.datasets.fashion_mnist
    (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

    x_train = x_train / 255.0
    x_test = x_test / 255.0

    os.makedirs(data_dir, exist_ok=True)

    with open(os.path.join(data_dir, 'x_train.pickle'), 'wb') as f:
        pickle.dump(x_train, f)

    with open(os.path.join(data_dir, 'y_train.pickle'), 'wb') as f:
        pickle.dump(y_train, f)

    with open(os.path.join(data_dir, 'x_test.pickle'), 'wb') as f:
        pickle.dump(x_test, f)

    with open(os.path.join(data_dir, 'y_test.pickle'), 'wb') as f:
        pickle.dump(y_test, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='kubeflow MNIST preprocess script')
    parser.add_argument('--data_dir', help='path to images and labels')

    args = parser.parse_args()
    preprocess(data_dir=args.data_dir)
