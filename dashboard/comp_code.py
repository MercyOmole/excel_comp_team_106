import numpy as np



#compare two files of any given number of rows but same number of columns
def rem(sheet1,sheet2):
        """Process dataframes uploaded by users and compares to remove duplicates.
        Returns a single dataframe"""
        #check for row lenght
        c = len(sheet1)
        d= len(sheet2)
        if c == d:
            #if number of rows match, compare them and an array Boolean of False and True
            comparison_values = sheet1.values == sheet2.values
            #assign the rows and columns respectively after getting their indexes from all false values
            rows,cols = np.where(comparison_values == False)
            #loop over them to get a list of tuples from the zipped values
            for item in zip(rows,cols):
                #assigning a empty value each row by iloc
                sheet1.iloc[item[0],item[1]] = '*{}'.format("-")
            #return edited dataframe
            return sheet1  
        else:
            if c>d:
                #if rows are mismatched, get the range of rows
                w = range(d,c)
                #match rows by appending empty rows
                sheet2 = sheet2.append(sheet1.reindex(list(w))) 
                comparison_values =sheet1.values == sheet2.values
                rows,cols = np.where(comparison_values == True)
                for item in zip(rows,cols):
                    sheet1.iloc[item[0],item[1]] = '*{}'.format('-')
                return sheet1
            elif d>c :
                w= range(c,d)
                #match row
                sheet1 = sheet1.append(sheet1.reindex(list(w))) 
                comparison_values =sheet1.values == sheet2.values
                rows,cols = np.where(comparison_values == True)
                for item in zip(rows,cols):
                    sheet1.iloc[item[0],item[1]] = '*{}'.format('-')
                sheet1 = sheet1.drop(w)
                return sheet1



#compare two files of any given number of rows but same number of columns
def high(sheet1,sheet2,flag):
        """Process dataframes uploaded by users and compares to highlight duplicates
        and asteric differnces. Returns a single dataframe"""
        #check for row lenght
        c = len(sheet1)
        d= len(sheet2)
        if c == d:
            #if number of rows match, compare them and an array Boolean of False and True
            comparison_values = sheet1.values == sheet2.values
            #assign the rows and columns with unmatched values respectively after getting their indexes
            rows,cols = np.where(comparison_values == False)
            #confirm if to merge sheets or not
            if flag == 'merge':
                #loop over them to get a list of tuples from the packed values after zipping
                for item in zip(rows,cols):
                    #assigning 2 differerence values from both sheets showing mismatch
                    sheet1.iloc[item[0],item[1]] = '*{} --> {}'.format(sheet1.iloc[item[0],item[1]],
                                                                       sheet2.iloc[item[0],item[1]])
                #return edited dataframe
                return sheet1
            else:
                for item in zip(rows,cols):
                    # adding an steric to the initial value at index
                    sheet1.iloc[item[0],item[1]] = '*{}'.format(sheet1.iloc[item[0],item[1]])
                return sheet1  
        else:
            if c>d:
                w = range(d,c)
                #match row
                sheet2 = sheet2.append(sheet1.reindex(list(w))) 
                comparison_values = sheet1.values == sheet2.values
                rows,cols = np.where(comparison_values == False)
                if flag == 'merge':
                    for item in zip(rows,cols):
                        sheet1.iloc[item[0],item[1]] = '*{} --> {}'.format(sheet1.iloc[item[0],item[1]],
                                                                       sheet2.iloc[item[0],item[1]])
                    return sheet1
                else:
                    for item in zip(rows,cols):
                        sheet1.iloc[item[0],item[1]] = '*{}'.format(sheet1.iloc[item[0],item[1]])
                    return sheet1
            elif d>c :
                w= range(c,d)
                #match row
                sheet1 = sheet1.append(sheet1.reindex(list(w))) 
                comparison_values = sheet1.values == sheet2.values
                rows,cols = np.where(comparison_values == False)
                if flag == 'merge':
                    for item in zip(rows,cols):
                        sheet1.iloc[item[0],item[1]] = '*{} --> {}'.format(sheet1.iloc[item[0],item[1]],
                                                                       sheet2.iloc[item[0],item[1]])
                    return sheet1
                else:
                    for item in zip(rows,cols):
                        sheet1.iloc[item[0],item[1]] = '*{}'.format(sheet1.iloc[item[0],item[1]])
                    sheet1 = sheet1.drop(w)
                    return sheet1