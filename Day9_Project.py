# Basic Calculator
# M.R. Sorell
# March 2021

import simplegui

# inititate global variables

store = 12
operand = 3
total = 0

# define functions that manipulate global variables
def output():
    print "Store: ",  store
    print "Operand: ", operand
    print "Total: ", total
    print ""
     
def swap():
    global store, operand
    store, operand = operand, store
    output()
    
def add():
    global store, operand, total
    total = store + operand
    output()
    
def mul():
    global store, operand, total
    total = store * operand
    output()  
    
def div():
    global store, operand, total
    total = store / operand
    output()  
    
def mod():
    global store, operand, total
    total = store % operand
    output()  
    
def sub():
    global store, operand, total
    total = store - operand
    output()
    
def clear():
    global  operand, total
    total = 0
    operand = 0
    output()


def enter_operand(imp):
    global operand
    operand = int(imp)
    output()

def enter_store(imp):
    global operand
    operand = int(imp)
    output()    

# create frame
canvas_width = 400
canvas_height = 400
frame = simplegui.create_frame(" SimpleGUI Calculator First Draft", canvas_width, canvas_height)

frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Subtract", sub, 100) 
frame.add_button("Multiply", mul, 100)
frame.add_button("Division", div, 100) 
frame.add_button("Modulus", mod, 100) 
frame.add_button("Clear", clear, 100) 
frame.add_input("Enter Operand", enter_operand, 100)
frame.add_input("Enter Store", enter_store, 100)
    
output()
swap()
swap()
