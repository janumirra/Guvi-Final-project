
import pandas as pd
list1=[2,4,5,6,7,8,9,12,43,2,3,65,71]
#list2=[1,2,3,4,5,6,7,8,9,10,11,12,13]
column=["example1"]
map_df=pd.DataFrame(list1,columns=column)
print(map_df)
'''
def my_mapp(cap_df):
    for col in cap_df.columns:
        if cap_df[col].values in range(1,11):
            cap_df[col].values==1
        elif cap_df[col].values()>0 & cap_df[col].values not in range(1,11):
            cap_df[col].values==2
        else:
            cap_df[col].values==cap_df[col].values
    return cap_df 
final_df= my_mapp(cap_df)
print(final_df)
'''




#map_df=df.drop(columns=['Cust_ID', 'Gender'])
for col in map_df.columns:
  my_dict = {map_df.example1.between(1,(map_df.example1.max())//2) : 1,
             map_df.example1.between((map_df.example1.max())//2 ,map_df.example1.max()) : 2}
  map_df.example1 = map_df.example1 .map(my_dict)

print(map_df)