import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#CITIES = ['Chicago' , 'new yourk' ,'washington']
#DAYS =[sunday , monday , tuesday , wedensday , thursday , friday, saturday] ..\n
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    #Using while loops
    while True:
        city = input("Choose the city you would like to filter\n ...chicgo , new york city , washington\n")
        if city not in ('chicago' , 'new york city' , 'washington'):
            print("Please choose only one of these three cities : chicago , new york city , washington")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("\nAny particular month you would like to filter from?....\
    [january , february , march , april , may , june ,  or type in 'all' ] ....")
        if month not in ('january', 'february','march','april','may','june' ,'all'):
            print("Please try again")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input("\nIf you're lookinf for choosing a say \n ..please choose one of the week days \
     [sunday , monday , tuesday , wedensday , thursday , friday, saturday] ..\n ")
        if day not in ('sunday' ,'monday','tuesday' ,'wedensday','thursday','friday','saturday'):
            print("You might have a spelling errorr , please choose on the of the week days as mentioned :\
     [sunday , monday , tuesday , wedensday , thursday , friday, saturday] ..\n")
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data files in csv file by using Pandas
    df = pd.read_csv(CITY_DATA[city])
    

    #convert start time to to_datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])

    ###############
    #Month and Day of the week
    #extract both
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter
    #MONTHS , using index
    #course
    if month !='all':
        month =['january' ,'february','march','april','may' ,'june']
        month = month.index(month)+1

        df=df[df['month'] == month] #new data frame

        #day_of_week filter
        if day !='all':
            df=df[ df['day_of_week'] == day.title()]




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    mc_month=df['month'].mode()[0]
    print("Common Month used : " , mc_month)

    # display the most common day of week
    mc_dweek =df['day_of_week'].mode()[0]
    print("Most Common Day of week is :" , mc_dweek)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mc_hour =df['hour'].mode()[0]
    print("Most Common Hour is :" , mc_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("Common Used Start Station is :" , start_station)


    # display most commonly used end station
    Cend_station = df['End Station'].value_counts().idxmax()
    print("Common Used End Station is : " , Cend_station)


    # display most frequent combination of start station and end station trip
    #Combine both
    Comb_station = df.groupby(['Start Station' , 'End Station']).count()
    print("Most commonly used End and Start statiobns are : " , start_station , Cend_station)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    T_travel_time = sum(df['Trip Duration'])
    print("The total travel time in Days is : " , T_travel_time/86400)


    # display mean travel time
    M_travel_time =df['Trip Duration'].mean()
    print("Mean Travel time in miutes is : " , M_travel_time/60)




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    usr_t =df['User Type'].value_counts()
    print("Counts of User Types are :" ,usr_t)


    # Display counts of gender
    try:
        g_ty=df['Gender'].value_counts()
        print("\n Gender Types :" , g_ty)
    except KeyError:
        print("\n No data Avilable....")


    # Display earliest, most recent, and most common year of Birth
    #Earliest year of birth
    try:
        erl_year= df['Birth Year'].min()
        print("Most Earliest Year :" , erl_year)
    except KeyError:
        print("No Data Avilable ....\n")



    #Most recent year of birth
 
    
    try:
        rcnt_year = df['Birth Year'].max()
        print("\n Most Recent year of birth is : " , rcnt_year)
    except KeyError:
            print("No Data Avilable ....")

    #Most common year of birth
    try:
        common_year = df['Birth Year'].value_counts().idxmax()
        print("\n Most Common Year of Birth is : " ,common_year)
    except KeyError:
            print("No Data Avilable ....")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
