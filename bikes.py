import time
import pandas as pd
import numpy as np
# This program is available for these three cities#
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter one of these three available cities to validate the information Chicago, New York City or Washington: ').lower()

    while city not in CITY_DATA:
        print('The city you entered is not available, please enter one of the three options.')
        city = input('Enter one of these three available cities to validate the information Chicago, New York City or Washington: ').lower()
    print('the city you chose is: {}'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA=('all','january', 'february', 'march', 'april', 'may', 'june')

    month = input('Enter a month between January and June or enter all: ').lower()

    while month not in MONTH_DATA:
        print ('the month I entered is wrong, please try again.')
        month = input('Enter a month between January and June or enter all: ').lower()
    print('the month you chose is: {}'.format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA=('all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

    day = input('Enter the day of the week you want to validate or enter all: ').lower()

    while day not in DAY_DATA:
        print ('the day entered is wrong, please try again.')
        day = input('Enter the day of the week you want to validate or enter all: ').lower()
    print('the day you chose is: {}'.format(day))
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
    df = pd.read_csv('{}.csv'.format(city).replace(' ', '_'))
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('\nThe Most Frequent month of Travel is {}\n'.format(popular_month))

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('\nThe Most Frequent day of Travel is {}\n'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe Most Frequent hour of Travel is {}\n'.format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#ONLY Stations of bikes#
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    nom_count_dict = {}

    for StartStation in df['Start Station']:
        if StartStation not in nom_count_dict:
            nom_count_dict[StartStation] = 1
        else:
            nom_count_dict[StartStation] += 1

    highest_count = max(nom_count_dict.values())

    most_start = [key for key, value in nom_count_dict.items() if value == highest_count]
    print('\nThe most popula station of start is {}'.format(most_start))

    # TO DO: display most commonly used end station
    nom_count_dict_end = {}

    for EndStation in df['End Station']:
        if EndStation not in nom_count_dict_end:
            nom_count_dict_end[EndStation] = 1
        else:
            nom_count_dict_end[EndStation] += 1

    highest_count_end = max(nom_count_dict_end.values())

    most_end = [key for key, value in nom_count_dict_end.items() if value == highest_count_end]
    print('\nThe most popular station of end is {}'.format(most_end))

    # TO DO: display most frequent combination of start station and end station trip
    frequency = df.groupby (['Start Station', 'End Station']).size().reset_index().rename(columns = {0: 'Count'}).sort_values(by=['Count'], ascending = False)
    max_frequency = frequency.head(1)
    print ('\nThe most frequency station on start and end are: \n {}'.format(max_frequency))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print('\n The total time of the Trip Duration is {}'.format(total_trip))

    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()
    print('\nThe mean of the Trip Duration is {}'.format(mean_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('the types of users are: \n{}' .format(user_types))

    # TO DO: Display counts of gender

    while True:
        try:
            gender_types = df['Gender'].value_counts()
            print('The use for each gender is: \n{}' .format(gender_types))
            max_birth_year = df.groupby(['Gender'])['Birth Year'].max()
            min_birth_year = df.groupby(['Gender'])['Birth Year'].min()
            mode_birth_year = df['Birth Year'].mode()
            print ('1. The most recent year of birth by gender is: {}\n2. The most earliest year of birth by gender is: {}\n3. The most common is: {}'.format(min_birth_year, max_birth_year, mode_birth_year))

            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)

            break
        except:
            print('\nIn the data the field the gender column does not exist, for this reason there are no statistics for this field')
            break

    # TO DO: Display earliest, most recent, and most common year of birth

#Asking 5 lines of the raw data and more, if they want#
def data(df):
    raw_data = 0
    while True:
        answer = input("Do you want to see the raw data? Yes or No").lower()
        if answer not in ['yes', 'no']:
            answer = input("You wrote the wrong word. Please type Yes or No.").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("Do you want to see more? Yes or No").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return
def main():
    city = ""
    month = ""
    day = ""
    while True:
    city,month,day = get_filters().lower().
    df = load_data(city,month,day)

    other_caractheristics (df)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    data(df)
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
            break
if __name__ == "__main__":
 main()
