print("        PROJECT OF INFORMATICS PRACTICES 2020-2021        ")
import pandas as pd
import matplotlib.pyplot as plt
print(                          '''DATAFRAME'''                  )
Dataframe = pd.read_csv("C:\\Users\\sony\\Desktop\\Googleplay.csv")
New=Dataframe.iloc[[43,68,118,148,198,315,376,718,9152,9883],[0,2,3,4,5]]
print(New)
print(          "MENU FOR OPERATIONS IN DATAFRAME"      )
print("1.MANIPULATING THE DATA")
print("2.ANALYSING THE DATA")
print("3.VISUALISING THE DATA")
print("4.EXIT")
ch=eval(input("Enter your choice "))
if (ch==1):
    print(''' 
          1.Delete a row
          2.Insert  a row
          3.Delete a column
          4.Insert a column''')
    subchoa=eval(input("Enter your choice"))
    if (subchoa==1):
       rowind=eval(input("Enter the row index which you want to delete"))
       print(New.drop([rowind],axis=0))
    elif(subchoa==2):
        print("Enter 5 column values for the new Row one by one first value should be string and rest 4 integer to match datatype")
        valc1=input("Value1")
        valc2=eval(input("Value2"))
        valc3=eval(input("Value3"))
        valc4=eval(input("Value4"))
        valc5=eval(input("Value5"))
        New.loc[11]=[valc1,valc2,valc3,valc4,valc5]
        print(New)
    elif(subchoa==3):
        colnm=eval(input("Enter the column name which you want to delete in inverted comma"))
        print(New.drop(colnm,axis=1))
    elif(subchoa==4):
        colmn=input("Enter name of new column all values should be integer")
        valc1=eval(input("Value1"))
        valc2=eval(input("Value2"))
        valc3=eval(input("Value3"))
        valc4=eval(input("Value4"))
        valc5=eval(input("Value5"))
        valc6=eval(input("Value6"))
        valc7=eval(input("Value7"))
        valc8=eval(input("Value8"))
        valc9=eval(input("Value9"))
        valc10=eval(input("Value10"))
        New[colmn]=[valc1,valc2,valc3,valc4,valc5,valc6,valc7,valc8,valc9,valc10]
        print(New)
    else:
        print("Invalid Entry")
if(ch==2):
    print('''
             1.Top Records
             2.Bottom Records
             3.Display a Particular Row
             4.Display a Particular Column
             5.To find Mean of Different Columns
             6.To find Sum of a Column
             7.Shape of dataframe
             8.Total Elements
             9.Value at any Particular Row,Column
             10.Data Types
             11.Transpose of dataframe
             12.Dimension Of dataframe
             13.Display Row index
             14.Display Column Index
             15.Extracting Data Row Wise(Horizontal)
             16.Extracting Data Column Wise(Vertical)''')
    subchob=eval(input("Enter Your Choice"))
    if(subchob==1):
        t=eval(input("Enter How Many Records from Top"))
        print(New.head(t))
    elif(subchob==2):
        b=eval(input("Enter How Many Records from Bottom"))
        print(New.tail(b))
    elif(subchob==3):
        ri=eval(input("Enter the row which you want to display"))
        print(New.iloc[ri-1])
    elif(subchob==4):
        ci=eval(input("Enter the column which you want to display"))
        print(New.iloc[:,ci-1])
    elif(subchob==5):
        print(New.mean(axis=0))
    elif(subchob==6):
        print(New.sum())
    elif(subchob==7):
        print(New.shape)
    elif(subchob==8):
        print(New.size)
    elif(subchob==9):
        rin=eval(input("Enter row index"))
        cin=eval(input("Enter Column Index"))
        print(New.iat[rin,cin])
    elif(subchob==10):
        print(New.dtypes)
    elif(subchob==11):
        print(New.T)
    elif(subchob==12):
        print(New.ndim)
    elif(subchob==13):
        print(New.index)
    elif(subchob==14):
        print(New.columns)
    elif(subchob==15):
        for(row,rowseries) in New.iterrows():
            print("Row Index:",row)
            print("Containing:")
            print(rowseries)
    elif(subchob==16):
        for(col,colseries) in New.iteritems():
            print("Column Index:",col)
            print("Containing:")
            print(colseries)
    else:
        print("Invalid Choice")
if(ch==3):
    print(''' 
          1.Pie Chart Between Apps and Rating  
          2.Bar Chart Between Apps and Rating 
            ''')
    subchoc=eval(input("Enter Your Choice"))
    if(subchoc==1):
        x=New["App"]
        y=New["Rating"]
        plt.pie(y,radius=2,autopct="%0.0f%%",shadow= True,startangle=90)
        plt.axis("equal")
        plt.title("RATING DISTRIBUTION OF DIFFERENT PLAY STORE APPS")
        plt.legend(x,loc="center right", bbox_to_anchor=(1.2, 0.2, 0.3, 0.7))
        plt.show()
    elif(subchoc==2):
        New=New.sort_values(by="Rating")
        x1=New["App"]
        y1=New["Rating"]
        plt.bar(x1,y1,color="c",align="center",width=0.2)
        plt.title("NO OF DOWNLOADS OF APPS")
        plt.xlabel("App")
        plt.ylabel("Rating")
        plt.show()
    else:
        print("Invalid Entry")
if(ch==4):
    pass
else:("Invalid Entry")
print('''                               HAVE A NICE DAY AHEAD !!!
                                                BYE BYE                          ''')

        
    
    
    
                    
    
