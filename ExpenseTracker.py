import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

class sana:
    
    times = pd.date_range('2012-10-01', periods=5, freq='1440min') #periods represent the size
    date=np.array(times,dtype = str)
  
    #print(times)
    #print(type(date))
    #print(date)
    date=np.char.strip(date,chars='00:00:00.000000000')
    date=np.char.strip(date,chars='T')
    #print(date)
    
    def calldur(date): 
        c = 0
        value = np.random.randint(0,30,5) #5 represent the size
        for i in date:
            ch = 0
            temp = 0
           
            print("For date : ",i)
            print("Enter value")
            while ch == 0:
                v = int(input())
                temp = temp+v
                print("The total value :",temp)
                ch = int(input("\nIf done press 1 else 0 to continue"))

            value[c] = float(temp)
            c=c+1
            ch = 0
        return value
    value = calldur (date)
    
    my_dict = {
            'date':date,
            'Expense':value
            }
    #print(my_dict)

    df = pd.DataFrame(my_dict)
    print(df)
        
    plt.plot(df['date'],df['call duration'])
    plt.show
    
    
