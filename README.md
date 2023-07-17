# Function Plotter

## Description
Desktop Application that plots function using PySide and Embedded matplolib

1. Python GUI program that plots an arbitrary user-entered function.
2. It takes a function of x from the user, e.g., 5*x^3 + 2*x.
3. It takes min and max values of x from the user.
4. The following operators are supported: + - / * ^.
5. GUI is simple and beautiful.
6. Appropriate input validation to the user input.
7. Messages are displayed to the user to explain any wrong input.


## How to run the project
1. You must have python 3.8
2. Go to the project directory
3. Install Requirements
```bash
pip install -r requirements.txt
```
4. Run the program
```bash
py main.py 
```


## Examples

### Working
![img.png](imgs%2Fimg.png)
![img_1.png](imgs%2Fimg_1.png)
![img_2.png](imgs%2Fimg_2.png)

### Not Working
- Invalid Input
![img_3.png](imgs%2Fimg_3.png)
- User not using x
![img_4.png](imgs%2Fimg_4.png)
- Zero Division
![img_5.png](imgs%2Fimg_5.png)
- Upper limit less than lower limit
![img_6.png](imgs%2Fimg_6.png)