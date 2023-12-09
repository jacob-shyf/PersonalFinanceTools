#!/usr/bin/env python3

from datetime import date

def get_days_until(target_date):
    # Define tuple containing the day in the 
    # year at the start of each month
    dpm = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

    # Get target day, month and year
    target_date = target_date.split('/')
    target_month = int(target_date[0])
    target_day = int(target_date[1])
    target_year = int(target_date[2])
    target_diy = dpm[target_month] + target_day     #Compute day in year

    # Get current day, month and, year
    current_date = str(date.today()).split('-')
    current_year = int(current_date[0])
    current_month = int(current_date[1])
    current_day = int(current_date[2])
    current_diy = dpm[current_month] + current_day  #Compute day in year

    # Figure out the number of days between current and target dates
    if current_year > target_year:
        # Target year is previous year
        nd = -1
    elif current_year == target_year:
        # Target year is this year
        if current_diy > target_diy:
            # Date already passed
            nd = -1
        else:
            nd = target_diy - current_diy
    else:
        # Target year is in future years
        ny = target_year - current_year - 1     #Years between

        # Days til end of year + years between + target day in year
        nd = (365 - current_diy) + (ny * 365) + target_diy

    return nd

def calculate_monthly_savings(goal, p, nd, ig):
    # Calculate the number of deposits that will be made
    num_contributions = (nd / 28) + 1
    num_contributions = int(num_contributions)
    
    # Calculate the principal with the interest that is accrued on it
    principal = p * ((1 + ig) ** (num_contributions - 1))

    # Calculate the interest that will be accrued on the monthly contribution
    interest = 0
    for i in range(0, num_contributions):
        interest += (1 + ig) ** (num_contributions - 1 - i)

    # Calculate monthly contribution
    monthly_contribution = (goal - principal) / interest

    return int(monthly_contribution)


if __name__ == '__main__':
    # Set your savings goal
    goal = int(input("Enter your savings goal: "))

    # Set savings goal target date
    target_date = input("Enter your target date (MM/DD/YYYY): ")

    # Get interest rate of savings account
    ir = float(input("Enter the APY of your savings account (XX.XX %): ")) / 100
    ig = (28 * ir * 0.75) / 365  # monthly inerest gained factor

    # Get current amount in savings
    p = int(input("Enter the current amount you have in savings: "))

    nd = get_days_until(target_date)
    monthly_savings = calculate_monthly_savings(goal, p, nd, ig)
    
    print('\nTo achieve your goal of saving $' + str(goal) + ' by ' + target_date + ', you must')
    print('contribute $' + str(monthly_savings) + ' each pay period.')


