# How to have parameter as args and kwargs
import pdb
'''
*args
The use : allows you to do is take in more 
arguments than the number of formal arguments 
that you previously defined.

observation: just print(*v )
output: tom lisa ikea
so we need to for loop it

'''
def args(var , *v):
    print(var)
    for name in v:
        print(name)



args("jack", "tom", 'Lisa',"ikea")



'''
*kwargs allows you to pass keyworded variable length of arguments to a function.
You should use **kwargs if you want to handle named arguments in a function




'''
def kwargs(**v):
    for key, value in v.items():
        print(f"{key} = {value}")

kwargs( args1 = 4 , args2 = 10 , args3 = "tom")







# how to pass kwarg and args as arguments
def test(args1 ,args2,args3):
    print("args1:", args1)
    print("args2:", args2)
    print("args3:", args3)


names ={"args1" : 4 , "args2": 10 , "args3" : "tom"}

# See how we put ** before the dictionary made
test(**names)
arg = ("hello", "how are you", "lol hogiya")
test(*arg)

# practise
# Aim make a calcultor 



def calculator(num , *number):

 if(not num.isdigit()):
     if(num == '*'):
        x = 1
        for numb in number:
            x =numb * x
     if(num == '+'):
       x = 0
       for numb in number:
        x =numb + x
     if(num == '-'):
        x = 0
        for numb in number:
         x =numb - x
     if(num == '/'):
        x = 1
        for numb in number:
            x =numb / x

 print(x)

arg = (1,2,3,4,10)
calculator("/",*arg)
comp = (1,'+' ,2, '-', 2, '*',5, '/',10)
i = 0
x = 0
while(i < len(comp)):
    if(i ==1):
        if(not i % 2 == 0):
            
            if(not comp[i].isdigit()):
                if(comp[i] == '*'):
                    
                    x = comp[i-1] * comp[i+1]   
                elif(comp[i] == '+'):
                    
                    x =  comp[i-1] + comp[i+1]   
                elif(comp[i] == '-'):
                
                    x = comp[i-1] - comp[i+1]    
                elif(comp[i] == '/'):
                
                    x =  comp[i-1] / comp[i+1]
            i = i+1 
        
            
        else:
            i = i+1


    else:
          if(not i % 2 == 0):

            if(not comp[i].isdigit()):
                if(comp[i] == '*'):
                    
                        x = x* comp[i+1]   
                elif(comp[i] == '+'):
                    
                        x =  x + comp[i+1]   
                elif(comp[i] == '-'):
                    
                    x = x - comp[i+1]    
                elif(comp[i] == '/'):
                    
                    x = x / comp[i+1]
                i = i+1 


          else:
            i = i+1





    if(i == len(comp)-1):
        print(x)
  

 
            
                

# order of using *args **kwargs and formal args
# So if you want to use all three of these in functions then the order is
# some_func(fargs, *args, **kwargs)








