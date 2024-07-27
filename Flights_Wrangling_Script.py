########################
# Author: Fred Lindsey #
########################

# 1. Wrangle Function

def wrangle_airlines_datset(file_path, output_file_path):

    """ This function takes an input .csv file path as an argument from the FAA airlines dataset, then converts that file into a dataframe.
    The function also takes to write location as an argument, for the output CSV destination.

    Next, the columns that are 100% null are removed from the dataset. For this dataset those columns can be accessed as the list, 'rem_cols_list'.

    Next, duplicate columns with data that are identical to the data of another column are removed. This list can be accessed as 'dup_cols'.

    The output of the function is a CSV files, called "df_flights_wrangled_again.csv"
    """

    # necessary libraries
    import os
    import pandas as pd
    from sklearn.model_selection import train_test_split

    #load file from CSV
    if os.path.exists(file_path):
        # check for the file path
        print(f"{file_path} exists, creating dataframe from local file.")
        # create df if found locally
        df_flights = pd.read_csv(file_path)
    else:
        print(f"{file_path} not found locally, go to 'https://transtats.bts.gov' to retrieve data set.")
    
    print(df_flights.shape)

    # Finding and removing 100% null columns. Start by generating a list with null proportions for any column with nulls
    na_list = df_flights.isna().mean()
    na_dict = {}

    for i, val in enumerate(na_list):
        if val > 0:
            na_dict[df_flights.columns[i]] = val

    full_nulls_prop_df = pd.DataFrame.from_dict(na_dict, orient = "index")

    # removing rows where flights were cancelled

    # grab the ones that are 100% null and put them in a dataframe
    complete_nulls = full_nulls_prop_df[full_nulls_prop_df[full_nulls_prop_df.columns[0]]==1]
    
    # make that df a list that we can drop from the master dataframe
    rem_cols_list = complete_nulls.index.tolist()
    df_flights_wrangled = df_flights.drop(columns = rem_cols_list)
    
    #drop the columns
    useless_cols = df_flights_wrangled.filter(regex=r"^Div").columns
    df_flights_wrangled_v2 = df_flights_wrangled.drop(columns = useless_cols)

    print("Shape at Wrangling step 2:", df_flights_wrangled_v2.shape)

    # next add a list of columns that are purely duplicate information
    dup_cols = ['Month', 'Operated_or_Branded_Code_Share_Partners', 'IATA_Code_Marketing_Airline','Duplicate', 'Flight_Number_Marketing_Airline',
                'Marketing_Airline_Network', 'DOT_ID_Operating_Airline',  'Tail_Number', 'OriginAirportID', 'OriginAirportSeqID', 'OriginCityMarketID', 
                'OriginCityName', 'OriginState', 'OriginStateFips', 'OriginStateName', 'OriginWac', 'DestAirportID',
                'DestAirportSeqID', 'DestCityMarketID', 'DestCityName', 'DestState', 'DestStateFips',
                'DestStateName', 'DestWac', 'Flights', 'FirstDepTime', 'TotalAddGTime', 'LongestAddGTime', 'Operating_Airline.' ]


    # columns we do not need for our model explaining departure delays
    model_drops = ['FlightDate', 'Flight_Number_Operating_Airline', 'CRSDepTime', 'DepDelay', 'DepDel15', 'DepartureDelayGroups', 'WheelsOff',
                   'WheelsOn', 'CRSArrTime', 'ArrTime', 'ArrDelay', 'ArrDelayMinutes', 'ArrDel15', 'ArrivalDelayGroups', 'CRSElapsedTime',
                   'ActualElapsedTime', 'TaxiIn']
    
    cols_to_drop = dup_cols + model_drops

    # now drop those duplicates as well
    df_flights_wrangled_again = df_flights_wrangled_v2.drop(columns=cols_to_drop)
    print("Shape at Wrangling step 3:", df_flights_wrangled_again.shape)

    # remove rows where cancelled = Y, remove cancelled columns
    # remove opeating_airline., IATA Code

    # Filter the DataFrame
    df_flights_wrangled_again = df_flights_wrangled_again[(df_flights_wrangled_again['Cancelled'] == 0) & (~df_flights_wrangled_again['DepDelayMinutes'].isna())]

    # Drop the specified columns
    df_final = df_flights_wrangled_again.drop(columns=['Cancelled', 'CancellationCode', 'DOT_ID_Marketing_Airline'])

    # Check the proportion of missing values in 'DepDelayMinutes'
    missing_mean = df_final['DepDelayMinutes'].isna().mean()
    print(f"Checking departure delay for missing values, the proportion of missing values is {missing_mean}")

    #load file from CSV
    if os.path.exists(output_file_path):
    # check for the file path
        print(f"{output_file_path} exists, rename output variable in function, or delete CSV to save a different version")
    else:
        print(f"{output_file_path} not found locally, writing to CSV now. Avg time to write is 2.5 - 3 mins.")
        df_final.to_csv(output_file_path, index=False)
        print(f"{output_file_path} successfully written to CSV.")
    

  


#-----------------------------------------------------------------

# 2. Train Test Split Function (60/30/20), with Stratification

def airlines_train_test_split(input_path):
    """ This function takes in the wrangled airlines dataset from the previous function, and outputs the split dataset in three CSVs, airlines_train,
    airlines_validate, and airlines_test. 
    
    The split is 60/30/10. 
    
    The dataset is stratified on 'Origin', 'Airline'.
    """

    # libraries
    import os
    import pandas as pd
    from sklearn.model_selection import train_test_split

    df = pd.read_csv(input_path)

    #Rename the airline column
    df = df.rename(columns={'IATA_Code_Operating_Airline':'Airline'})

    df['stratify_combined'] = df[['Origin','Airline']].astype(str).agg('-'.join, axis=1)
    print("Stratification variables set")

    train_val_df, test_df = train_test_split(df, test_size=0.1, stratify=df['stratify_combined'], random_state=42)
    print("Train test split complete")

    train_df, validate_df = train_test_split(train_val_df, test_size=0.333, stratify=train_val_df['stratify_combined'], random_state=42)
    print("Train validate split complete")

    train_df = train_df.drop(columns =['stratify_combined'])
    validate_df = validate_df.drop(columns =['stratify_combined'])
    test_df = test_df.drop(columns =['stratify_combined'])

    print(f"The length of the training dataset is {len(train_df)}")
    print(f"The length of the validate dataset is {len(validate_df)}")
    print(f"The length of the test dataset is {len(test_df)}")

    df_dict = {'Flights_Train': train_df,
           'Flights_Validate': validate_df,
           'Flights_Test': test_df}

    for df_name, df in df_dict.items():
        print(df_name)
        # write to CSV
        if os.path.exists(f"{df_name}.csv"):
        # check for the file path
            print(f"{df_name} exists and is saved")
        else:
            print(f"{df_name} not found locally, writing to CSV now. Avg time to write is 2.5 - 3 mins.")
            df.to_csv(f"{df_name}.csv", index=False)
            print(f"{df_name} successfully written to CSV.")




#-----------------------------------------------------------------

# 3. Executing Functions
df_csv = wrangle_airlines_datset("./Data_Files/Flight_Data_MASTER.csv", "./Data_Files/Flights_Wrangled.csv")
airlines_train_test_split("./Data_Files/Flights_Wrangled.csv")