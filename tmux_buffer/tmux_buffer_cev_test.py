import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm_notebook
from importlib import resources
import io 

def cleandata(data):    
    data = data.rename(columns={0: 'Data'})
    data = data[data['Data'].str.contains('Model|Total|bd')==False]
    data.to_csv(r'cleanedfinal.txt', header=None, index=None, sep=' ', mode='a')


def extractdata(data):   
    data = data.rename(columns={0: 'Data'})

    new_df = pd.DataFrame(columns = ['Fold', 'Epoch', 'Train_Acc', 'Temp_Test_Acc'])

    for idx in tqdm_notebook(range(0,len(data),4)):
        fold = (data.iloc[idx])['Data']
        epoch = (data.iloc[idx+1])['Data']
        train = (data.iloc[idx+2])['Data']
        test = (data.iloc[idx+3])['Data']
        
        # https://pythonexamples.org/pandas-dataframe-add-append-row/
        
        fold_val = fold.rsplit(' ', 1)[1][:]

        epoch_val = epoch.rsplit(':', 1)[1][:]
    
        train_acc_val = train.rsplit(" ", 1)[1][:]
        
        test_acc_val = test.rsplit(" ", 2)[1]
        
        # Declare Dictionary to append to dataframe
        new_row = {'Fold': fold_val, 'Epoch': epoch_val, 'Train_Acc': train_acc_val, 'Temp_Test_Acc': test_acc_val}
        new_df = new_df.append(new_row, ignore_index=True)

    new_df["Test_Acc"] = new_df["Temp_Test_Acc"].str.split("/").apply(lambda x: float(x[0]) / float(x[1]))
    new_df = new_df.drop("Temp_Test_Acc", axis=1)
    new_df = new_df.round(decimals = 4)
    new_df.to_csv('extractedfinal.csv', index=False)



def Fold0(new_df):
    new_df0=new_df.loc[new_df['Fold'] == 0]
    ax = plt.gca()
    new_df0.plot(kind='line',x='Epoch', y='Train_Acc',ax=ax)
    new_df0.plot(kind='line',x='Epoch', y='Test_Acc', color='red', ax=ax)
    plt.show()

def Fold1(new_df):
    new_df1=new_df.loc[new_df['Fold'] == 1]
    ax = plt.gca()
    new_df1.plot(kind='line',x='Epoch', y='Train_Acc',ax=ax)
    new_df1.plot(kind='line',x='Epoch', y='Test_Acc', color='red', ax=ax)
    plt.show()

def Fold2(new_df):
    new_df2=new_df.loc[new_df['Fold'] == 2]
    ax = plt.gca()
    new_df2.plot(kind='line',x='Epoch', y='Train_Acc',ax=ax)
    new_df2.plot(kind='line',x='Epoch', y='Test_Acc', color='red', ax=ax)
    plt.show()

def Fold3(new_df):
    new_df3=new_df.loc[new_df['Fold'] == 3]
    ax = plt.gca()
    new_df3.plot(kind='line',x='Epoch', y='Train_Acc',ax=ax)
    new_df3.plot(kind='line',x='Epoch', y='Test_Acc', color='red', ax=ax)
    plt.show()

def Fold4(new_df):
    new_df4=new_df.loc[new_df['Fold'] == 4]
    ax = plt.gca()
    new_df4.plot(kind='line',x='Epoch', y='Train_Acc',ax=ax)
    new_df4.plot(kind='line',x='Epoch', y='Test_Acc', color='red', ax=ax)
    plt.show()