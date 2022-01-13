import numpy as np
import joblib
import argparse
import pickle


def test_model(x_test, y_test, model_dir, output_dir):
    x_test_data = pickle.load(x_test)
    y_test_data = pickle.load(y_test)

    model = joblib.load('{}/model.pkl'.format(model_dir))
    result = model.evaluate(x_test_data, y_test_data)

    with open('{}/output.txt'.format(output_dir), 'a') as f:
        f.write(str(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_test')
    parser.add_argument('--y_test')
    parser.add_argument('--model_dir')
    parser.add_argument('--output_dir')
    args = parser.parse_args()
    test_model(args.x_test, args.y_test, args.model_dir, args.output_dir)
