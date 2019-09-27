import argparse
import data_viz
import get_data


def getparser():
    """
    This function handles the argument from command line

    Return:
    args: args structure that collects argument from command line

    """
    parser = argparse.ArgumentParser(description='Data visualization')
    parser.add_argument('--out_file', type=str, default='name.png',
                        help='an absolute path for output image')
    parser.add_argument('--plot_type', type=str, default='',
                        help='The plot type for data visualization')
    parser.add_argument('--col_num', type=int, default=0,
                        help='The column number.')
    args = parser.parse_args()
    return args


def main():
    args = getparser()
    data = get_data.read_stdin_col(args.col_num)
    if args.plot_type == 'boxplot':
        data_viz.boxplot(data, args.out_file)
    elif args.plot_type == 'histogram':
        data_viz.histogram(data, args.out_file)
    elif args.plot_type == 'combo':
        data_viz.combo(data, args.out_file)
    else:
        raise ValueError('Legal list for plot_type: boxplot, histogram, combo')


if __name__ == '__main__':
    main()
