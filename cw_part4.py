# Author: Chenyu Liu and Lindi Wei

# Date of the first creation: 2023-1-18

R = 0
button = False  # Button is used to set the drop-down box. 
                # If file input is selected, manual input will fail. Otherwise, file input will fail.
d = 0
lambda_value = 0
U = 0

app = tk.Tk()  # Create interface
app.title('U calculator')  # Interface title
app.geometry("500x200+250+250")  # Set the interface size, width, height and position on the screen
path = tk.StringVar()  # Read the file text box

def choosefile():
    if button == False:
        path_ = tk.filedialog.askopenfilename()  # Select  the file path
        path.set(path_)  # Modify the path value
        readExcel()  # call function


def readExcel():
    global R
    global button
    global U
    print(path.get())
    with open(path.get(), 'r', encoding='utf-8') as fp:  # Read the selected CSV file
        data = csv.reader(fp)  # Read file information to data
        i = 0
        for row in data:  # Output in line, the first line is d, the second line is λ
            if i == 0:  # If it's the first row, it's assigned to d
                d = row
                i = i + 1
            else:
                lambdas = row  # The second line is assigned to the lambdas
    for i in range(len(d)):  # Each d is divided by lambda and then summed over R
        R = R + float(d[i]) / float(lambdas[i])
    U = float(1 / R)  # 1/RFind the U value
    # Uvalue()
    button = True


file_path_label = tk.Label(app, text='file_path')  # Set the file path title
file_path_label.place(x=5, y=5)  # Set title position

file_path_entry = tk.Entry(app, state='readonly', width=50, textvariable=path)  # Set the file path text box
file_path_entry.place(x=60, y=5, height=30)  # Text box position
file_button = tk.Button(app, text='choosefile', command=choosefile)  # Set the file selection button and call choosefile() function
file_button.place(x=420, y=5)

g = tk.StringVar()  # g represents a string that can be assigned to a text box and used to change the value of the text box. Then, simply changing g can change the value of the corresponding text box
num_label = tk.Label(app, text='amount')
num_label.place(x=25, y=40)
num_label_entry = tk.Entry(app, width=30, textvariable=g)
num_label_entry.place(x=60, y=40, height=30)

a = tk.StringVar()  # Same function as above
D_label = tk.Label(app, text='d')
D_label.place(x=25, y=85)
D_label_entry = tk.Entry(app, width=30, textvariable=a)
D_label_entry.place(x=60, y=80, height=30)


# Manually enter the function called to calculate U
def calculationU():
    global d
    global lambda_value
    global U
    if button:  # If the input is manual
        u = 0
        k = num_label_entry.get()  # Obtain the num text box and view the entered data quantity
        for i in range(int(k)):  # Cyclic input
            input_Lambda_D()  # Call the function with input D and λ
            g.set(str(int(k) - int(i) - 1))  # The quantity box value is reduced by one
            u = u + d / lambda_value  # u records the sum of the R's evaluated, and then assigns U to the reciprocal
        U = 1 / float(u)