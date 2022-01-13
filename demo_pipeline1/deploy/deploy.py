import argparse


def deploy_model(output_dir):
    print('deploying model', output_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_dir')
    args = parser.parse_args()
    deploy_model(args.output_dir)
