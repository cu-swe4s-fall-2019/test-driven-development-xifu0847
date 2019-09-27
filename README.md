# test-driven-dev
Test Driven Development

## Usage:
- Create stdin from bash:
```shell
$ bash gen_data.sh | python viz.py --plot_type=${TYPE} --out_file=${NAME} --col_num=${NUM}
```
- Create stdin with manual input(You need to input number in the console)
```shell
$ python viz.py --plot_type=${TYPE} --out_file=${NAME} --col_num=${NUM}
```
TYPE: should be one of the following - boxplot, histogram, combo
NAME: file name of your output
NUM: a valid column number. Should be in range (0, len(input_line)-1)

### math_lib:
math_lib is a module that provides two APIs for math calculation.

- list_mean: Calculate the mean of an input list
- list_stdev: Calculate the stdev of an input list

### get_data:
get_data is a module that provides one API reading stdin from console.

- read_stdin_col: Store an array of numbers selected at col_num position

### data_viz:
data_viz is a module that provides three APIs plotting visiable data given a list of data.

- boxplot: Draw a boxplot diagram and save it as a figure.
- histogram: Draw a histogram diagram and save it as a figure.
- combo: Draw one boxplot diagram and one histogram diagram in one figure and save it as out_file_name.

## Test

- Unit test: test_data_viz.py, test_get_data.py, test_math_lib.py
- Build Guardian: .travis.yml
