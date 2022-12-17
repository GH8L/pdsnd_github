import time
import pandas as pd
import numpy as np


#refeactoring edited 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


#add city , months , days

#start of week is sunday  , it can change
DAYS = ['sunday' , 'monday' , 'tuesday', 'wednseday' , 'thursday' , 'friday']

MONTHS = ['january' , 'february' , 'march' , 'april' , 'may' ,'june' , 'july' , 'august' ,'september' , 'october' , 'november' , 'December']

#3 cities added
CITIES=['chicago' , 'new yourk' , 'washington']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs #3 cities
   
    while True:
        city = input("Enter city name to Explore info from <(chicago , new yourk  city, washington>)\n").lower()
        if city in CITIES:
            break
        
    
    # TO DO: get user input for month (all, january, february, ... , june)

    month= get_user_input("enter a month name , or (All) to apply months to search filter" , MONTHS)
    
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day= get_user_input("enter day of the week (sunday ....friday) to apply to filter\n ",DAYS)   

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
    
    
    df=pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    #month . day , extraction. to create column
    #dataframes
    
    df['month']=df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday.name
    df['hour'] =df['Start Time'].dt.hour
    
    
    #use filtering , month
    
    if month!= 'all':
       month= MONTHS.index(month) +1
       df = df[df['month'] == month]
    
    
     #day
        
   if day!='all':
         df =df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
      most_common_month = df['month'].value_counts().idxmax()
        print("Most common month  :", most_common_month)

    # TO DO: display the most common day of week
most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
print("Most common day of week :",most_common_day_of_week)



    # TO DO: display the most common start hour

    most_common_start_hour=df['hour'].value_counts().idxmax()
    print("Most common start hour:",most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
most_common_start_station =df['Start Station'].value_counts().idxmax()
print("Most common start station:" , most_common_start_station)

    # TO DO: display most commonly used end station
most_common_end_statio = df['Endm Station'].value_counts().idxmax()
print("Most common used end station", most_common_end_station)



    # TO DO: display most frequent combination of start station and end station trip
    
    #merge end and start 
    
    most_common_start_end_station =df [[ 
       'Start Station' , 'End Station']].mode().loc[0]
    print("Most commonly used start , end station :{} ,{}".format(most_common_start_end_station[0] , Most_common_used_start_end_station[1]))
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
      total_travel = df['Trip Duration'].sum()
        
      print("total travel time :",total_travel)
    # TO DO: display mean travel time
    #same but add .mean()
    
    mean_travel=df['Trip Duration'].mean()
    print("mean travel time",mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types")
   user_counts =df['User Type'].value_counts()

    for index , user_count in enumerate(user_counts):
       print("count is  {} : {}".format(user_counts.index[index],user_count))
    

    # TO DO: Display counts of gender

    print("Counts of genders:")
    gender_counts = df['Gender'].value_counts()
    
    for index , gender_count in enumerate(gender_counts(:
                                                         print("gender counts is {} : {} ".format(gender_counts.index[index] ,gender_count))
     
    

    # TO DO: Display earliest, most recent, and most common year of birth 
                                                       most_common_year =df['Birth Year '].value_counts().idxmax() 
                                                        print("most common birth year:" , most_common_year)
                                                      
                                                        most_recent_year = df['Birth Year'].value_counts().idxmax()
print("Most recent birth year:",most_recent_year)
                                                        
                                                        most_earliest_year =df['Birth Year'].value_counts().idxmax()
                                                        print("Earliest birth year",most_earliest_year)
                                  
                                                        
                                                        
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
