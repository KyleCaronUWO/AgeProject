## Age mini project
## Created by Kyle Caron

## Collect Years from the user
start_year = input('Please enter the birth year:')
start_year = int(start_year)
end_year = input('Please enter the death or current year:')
end_year = int(end_year)

## Calculate years by subtracting death or current year (end_year) by birth year or start year.

age = (end_year - start_year)

print('The age is:', age)