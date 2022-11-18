import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/colors.csv')
print(df.shape)### Prints how many rows and columns

print(df.sort_values(by=['is_trans'], ascending=False)) ### shows transparent colors 't'


sets_df = pd.read_csv('data/sets.csv')
print(sets_df) ### Shows data in sets.csv


print(sets_df.sort_values('year').head()) ### We can sort values in year column and show top 5 value with .head()
print(sets_df[sets_df['year'] == 1959])  ### If we want to search values in specific year or value we can do it like this


print(sets_df.sort_values('num_parts', ascending=False).head())    ###  It shows top 5 values in num_parts column
                                                                     ### This code answers What is the most LEGO sets with number of parts



### How do the number of sets released in 1955 compare to the number of sets released in 2019?
sets_by_year = sets_df.groupby('year').count()
print(sets_by_year['set_num'].head()) ### Here we can see the number of sets released in 1955
print(sets_by_year['set_num'].tail()) ### Here we can see the number of sets released in 2019


#######################                       Matplotlib                   #############################

plt.plot(sets_by_year.index, sets_by_year.set_num)
plt.show()  ### In this plot we can see that after 2020 goes down cause the data has only few data in 2021
## We can slice our plot with using [:]
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])
plt.show() ### If you will have an error like "FutureWarning: " Dont worry! :D


### .agg() Function   ###

themes_by_year = sets_df.groupby('year').agg({'theme_id': pd.Series.nunique})

themes_by_year.rename(columns={'theme_id':'nr_themes'}, inplace=True)
print(themes_by_year.head())
print(themes_by_year.tail())


### Lets plot the number of themes released by year slicing the 2020 and 2021
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])
plt.show() ### Shows the plot

ax1 = plt.gca() # get the axis
ax2 = ax1.twinx() # create another axis that shares the same x-axis

# Add styling
ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color='green')
ax2.set_ylabel('Number of Themes', color='blue')

plt.show()

### How many parts did the average LEGO set released in 1954 compared to say, 2017?

### To find the average number of parts per set we can use '.groupby' and '.agg()'

parts_per_set = sets_df.groupby('year').agg({'num_parts': pd.Series.mean})
print(parts_per_set.head())
print(parts_per_set.tail())

##########           Scatter Plot             #############
plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])
plt.show()



themes_df = pd.read_csv('data/themes.csv')  ### Here we can see that in our csv there are names of LEGO themes

print(themes_df)    ### Uncomment it to see the data

###  Search the theme name 'Star Wars'

print(themes_df[themes_df['name'] == 'Star Wars']) ### Here we can see that we have 'id' for each theme
### [18] [158] [209] [261]



### If you saw in our sets.csv we have theme_id column
### Let's compare themes.csv 'id' with sets.csv 'theme_id'

print(sets_df[sets_df['theme_id'] == 18]) ### In our data in sets.csv we have names of LEGO sets Star Wars related

### We also can see them in this way
print(sets_df[sets_df.theme_id == 209])  ### By using "."

set_theme_count = sets_df["theme_id"].value_counts()
print(set_theme_count[:5])


###             Merging  (Combining) DataFrames      ####

### It would be nice to see combination of theme names with the number of sets per theme

set_theme_count = pd.DataFrame({'id':set_theme_count.index,
                                'set_count':set_theme_count.values})
print(set_theme_count.head())


merged_df = pd.merge(set_theme_count, themes_df, on='id')
print(merged_df[:3])



###               Bar Plot              #####

# plt.bar(merged_df.name[:10], merged_df.set_count[:10])
# plt.show() # We can do it like this but here as we can see there are some information is messed up and unreadable


# We have to configure

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])
plt.show()