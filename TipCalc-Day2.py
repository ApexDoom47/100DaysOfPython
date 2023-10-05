print('Welcome to the tip calculator.')

total = input('What was the total bill? $')

percent = int(
    input('What percentage tip would you like to give? 10, 12, or 15? '))

people = input('How many people to split the bill? ')

tip_percent = percent / 100

total_tip_amount = float(total) * float(tip_percent)

total_bill = float(total) + float(total_tip_amount)

bill_per_person = float(total_bill) / float(people)

print(f'Each person should pay: ${round(bill_per_person, 2)}')
