import time
import pandas as pd
import numpy as np
import datetime as dt


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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

    while True:
        city = input(
            " choose a city to search the data from (Chicago , New York City , Washington)".title())
        if city not in CITY_DATA:
            print(" invalid city please choose a city from the three provided ")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input(
            " please choose a month starting from january to june or type 'all'to show all months ".lower())
        month = ["january", "february", "march", "april", "may", "june"]
        if month not in month and month != "all":
            print(
                " please enter 'all' to show all five months or inter a month name from above!!")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "please type all to show the data for all days or type the name of the day you want".lower())
        days = [" saturday", "sunday", "monday",
                "tuesday", "wendesday", "thursday", "friday"]
        if day not in days and day != "all":
            print(" invalid input please try again ")
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

    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
    if month != 'all':
        months = month.index(month)+1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df["common_month"] = df["Start Time"].dt.month
    c_month = df["common_month"].mode()
    print(" The most common month :"+c_month)

    # TO DO: display the most common day of week
    df["common_day"] = df["Start Time"].dt.weekday_name
    c_day = df["common_day"].mode()
    print("Most common day of the Week:", c_day)

    # TO DO: display the most common start hour
    df["common_hour"] = df["Start Time"].dt.hour
    c_hour = df["common_hour"].mode()
    print("Most Common Start Hour:" + c_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df["Start Station"].mode()
    print("the most common start station is :"+start_station)

    # TO DO: display most commonly used end station
    end_station = df["End Station"].mode()
    print("the most common end station is :"+end_station)

    # TO DO: display most frequent combination of start station and end station trip
    comb_start_end = (df[start_station] + df[end_station].mode())
    print(" the most common combination of start station and end station :" + comb_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df["Trip Duration"].sum()
    print("the total trip duration : "+total_time)

    # TO DO: display mean travel time
    mean_time = df["Trip Duration"].mean()
    print("the average trip duration : "+mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_t = df["User Type"].value_counts()
    print(" the count of user types:"+user_t)

    # TO DO: Display counts of gender
    user_g = df["Gender"].value_counts()
    print(" the count of user types:"+user_g)

    # TO DO: Display earliest, most recent, and most common year of birth
    earlist = df["Birth Year"].min()
    common = df["Birth Year"].mode()
    last = df["Birth Year"].max()
    print(" the earlist year of birth:"+earlist)
    print(" the most common year of birth :" + common)
    print(" the most recent year of birth :"+last)

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